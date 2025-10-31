#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB v8.0 - ANALYTICS MODULE ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# ═══════════════════════════════════════════════════════════════════
# Advanced Analytics and Database Management
# ═══════════════════════════════════════════════════════════════════

import sqlite3
import json
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from collections import defaultdict
import os

class AnalyticsEngine:
    """Advanced analytics and database management"""
    
    def __init__(self, db_path: str = 'sms_bomb_analytics.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Sessions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone TEXT NOT NULL,
                start_time REAL NOT NULL,
                end_time REAL,
                total_waves INTEGER,
                total_attempts INTEGER,
                total_success INTEGER,
                total_failed INTEGER,
                success_rate REAL,
                mode TEXT,
                status TEXT
            )
        ''')
        
        # API attempts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS api_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER,
                api_name TEXT NOT NULL,
                timestamp REAL NOT NULL,
                success INTEGER NOT NULL,
                response_time REAL,
                error_message TEXT,
                FOREIGN KEY (session_id) REFERENCES sessions (id)
            )
        ''')
        
        # API statistics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS api_stats (
                api_name TEXT PRIMARY KEY,
                total_attempts INTEGER DEFAULT 0,
                total_success INTEGER DEFAULT 0,
                total_failed INTEGER DEFAULT 0,
                avg_response_time REAL DEFAULT 0,
                last_success_time REAL,
                last_fail_time REAL,
                success_rate REAL DEFAULT 0
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def start_session(self, phone: str, total_waves: int, mode: str) -> int:
        """Start a new bombing session"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO sessions (phone, start_time, total_waves, mode, status, 
                                 total_attempts, total_success, total_failed, success_rate)
            VALUES (?, ?, ?, ?, ?, 0, 0, 0, 0)
        ''', (phone, time.time(), total_waves, mode, 'running'))
        
        session_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return session_id
    
    def end_session(self, session_id: int, stats: Dict):
        """End a bombing session"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE sessions 
            SET end_time = ?, total_attempts = ?, total_success = ?, 
                total_failed = ?, success_rate = ?, status = ?
            WHERE id = ?
        ''', (
            time.time(),
            stats['total_attempts'],
            stats['success'],
            stats['failed'],
            stats['success_rate'],
            'completed',
            session_id
        ))
        
        conn.commit()
        conn.close()
    
    def record_attempt(self, session_id: int, api_name: str, success: bool, 
                      response_time: float = 0, error_message: str = None):
        """Record an API attempt"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Record attempt
        cursor.execute('''
            INSERT INTO api_attempts (session_id, api_name, timestamp, success, 
                                     response_time, error_message)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (session_id, api_name, time.time(), 1 if success else 0, 
              response_time, error_message))
        
        # Update API stats
        cursor.execute('''
            INSERT INTO api_stats (api_name, total_attempts, total_success, total_failed)
            VALUES (?, 1, ?, ?)
            ON CONFLICT(api_name) DO UPDATE SET
                total_attempts = total_attempts + 1,
                total_success = total_success + ?,
                total_failed = total_failed + ?,
                success_rate = CAST(total_success AS REAL) / total_attempts * 100
        ''', (api_name, 1 if success else 0, 0 if success else 1,
              1 if success else 0, 0 if success else 1))
        
        if success:
            cursor.execute('''
                UPDATE api_stats SET last_success_time = ? WHERE api_name = ?
            ''', (time.time(), api_name))
        else:
            cursor.execute('''
                UPDATE api_stats SET last_fail_time = ? WHERE api_name = ?
            ''', (time.time(), api_name))
        
        conn.commit()
        conn.close()
    
    def get_session_history(self, limit: int = 10) -> List[Dict]:
        """Get recent session history"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, phone, start_time, end_time, total_waves, total_attempts,
                   total_success, total_failed, success_rate, mode, status
            FROM sessions
            ORDER BY start_time DESC
            LIMIT ?
        ''', (limit,))
        
        sessions = []
        for row in cursor.fetchall():
            sessions.append({
                'id': row[0],
                'phone': row[1],
                'start_time': datetime.fromtimestamp(row[2]).strftime('%Y-%m-%d %H:%M:%S'),
                'end_time': datetime.fromtimestamp(row[3]).strftime('%Y-%m-%d %H:%M:%S') if row[3] else 'Running',
                'total_waves': row[4],
                'total_attempts': row[5],
                'total_success': row[6],
                'total_failed': row[7],
                'success_rate': row[8],
                'mode': row[9],
                'status': row[10]
            })
        
        conn.close()
        return sessions
    
    def get_api_statistics(self) -> List[Dict]:
        """Get API statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT api_name, total_attempts, total_success, total_failed, 
                   success_rate, last_success_time, last_fail_time
            FROM api_stats
            ORDER BY success_rate DESC
        ''')
        
        stats = []
        for row in cursor.fetchall():
            stats.append({
                'api_name': row[0],
                'total_attempts': row[1],
                'total_success': row[2],
                'total_failed': row[3],
                'success_rate': row[4],
                'last_success': datetime.fromtimestamp(row[5]).strftime('%H:%M:%S') if row[5] else 'Never',
                'last_fail': datetime.fromtimestamp(row[6]).strftime('%H:%M:%S') if row[6] else 'Never'
            })
        
        conn.close()
        return stats
    
    def get_performance_trends(self, days: int = 7) -> Dict:
        """Get performance trends over time"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cutoff_time = time.time() - (days * 24 * 60 * 60)
        
        cursor.execute('''
            SELECT 
                COUNT(*) as total_sessions,
                SUM(total_attempts) as total_attempts,
                SUM(total_success) as total_success,
                AVG(success_rate) as avg_success_rate
            FROM sessions
            WHERE start_time > ? AND status = 'completed'
        ''', (cutoff_time,))
        
        row = cursor.fetchone()
        
        trends = {
            'total_sessions': row[0] or 0,
            'total_attempts': row[1] or 0,
            'total_success': row[2] or 0,
            'avg_success_rate': row[3] or 0
        }
        
        # Get daily breakdown
        cursor.execute('''
            SELECT 
                DATE(start_time, 'unixepoch') as date,
                COUNT(*) as sessions,
                SUM(total_success) as success,
                AVG(success_rate) as avg_rate
            FROM sessions
            WHERE start_time > ? AND status = 'completed'
            GROUP BY DATE(start_time, 'unixepoch')
            ORDER BY date DESC
        ''', (cutoff_time,))
        
        trends['daily_breakdown'] = []
        for row in cursor.fetchall():
            trends['daily_breakdown'].append({
                'date': row[0],
                'sessions': row[1],
                'success': row[2],
                'avg_rate': row[3]
            })
        
        conn.close()
        return trends
    
    def export_to_json(self, output_file: str = 'analytics_export.json'):
        """Export analytics to JSON file"""
        data = {
            'export_time': datetime.now().isoformat(),
            'sessions': self.get_session_history(limit=100),
            'api_stats': self.get_api_statistics(),
            'trends': self.get_performance_trends()
        }
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        return output_file
    
    def export_to_csv(self, output_file: str = 'analytics_export.csv'):
        """Export session data to CSV"""
        import csv
        
        sessions = self.get_session_history(limit=1000)
        
        with open(output_file, 'w', newline='') as f:
            if sessions:
                writer = csv.DictWriter(f, fieldnames=sessions[0].keys())
                writer.writeheader()
                writer.writerows(sessions)
        
        return output_file
    
    def get_top_apis(self, limit: int = 10) -> List[Dict]:
        """Get top performing APIs"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT api_name, total_success, success_rate
            FROM api_stats
            WHERE total_attempts > 10
            ORDER BY success_rate DESC, total_success DESC
            LIMIT ?
        ''', (limit,))
        
        top_apis = []
        for row in cursor.fetchall():
            top_apis.append({
                'api_name': row[0],
                'total_success': row[1],
                'success_rate': row[2]
            })
        
        conn.close()
        return top_apis
    
    def get_worst_apis(self, limit: int = 10) -> List[Dict]:
        """Get worst performing APIs"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT api_name, total_failed, success_rate
            FROM api_stats
            WHERE total_attempts > 10
            ORDER BY success_rate ASC, total_failed DESC
            LIMIT ?
        ''', (limit,))
        
        worst_apis = []
        for row in cursor.fetchall():
            worst_apis.append({
                'api_name': row[0],
                'total_failed': row[1],
                'success_rate': row[2]
            })
        
        conn.close()
        return worst_apis
    
    def clear_old_data(self, days: int = 30):
        """Clear data older than specified days"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cutoff_time = time.time() - (days * 24 * 60 * 60)
        
        # Delete old sessions
        cursor.execute('DELETE FROM sessions WHERE start_time < ?', (cutoff_time,))
        
        # Delete orphaned attempts
        cursor.execute('''
            DELETE FROM api_attempts 
            WHERE session_id NOT IN (SELECT id FROM sessions)
        ''')
        
        conn.commit()
        conn.close()