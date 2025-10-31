#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB v8.0 - AI ENGINE MODULE ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# ═══════════════════════════════════════════════════════════════════
# Advanced AI Engine for Smart API Selection and Success Prediction
# ═══════════════════════════════════════════════════════════════════

import time
import random
from typing import List, Dict, Tuple, Optional
from collections import defaultdict, deque
from datetime import datetime, timedelta
import json
import os

class AIEngine:
    """Advanced AI Engine for intelligent bombing decisions"""
    
    def __init__(self):
        self.api_history = defaultdict(lambda: {
            'success': deque(maxlen=100),
            'fail': deque(maxlen=100),
            'response_times': deque(maxlen=50),
            'last_success_time': None,
            'last_fail_time': None,
            'consecutive_fails': 0,
            'best_time_of_day': None,
            'carrier_success': defaultdict(int)
        })
        self.session_data = {
            'start_time': None,
            'total_attempts': 0,
            'total_success': 0,
            'patterns_learned': []
        }
        self.learning_rate = 0.1
        self.history_file = 'ai_history.json'
        self.load_history()
    
    def load_history(self):
        """Load historical data from file"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    data = json.load(f)
                    # Restore basic stats
                    for api_name, stats in data.get('api_stats', {}).items():
                        self.api_history[api_name]['consecutive_fails'] = stats.get('consecutive_fails', 0)
                        self.api_history[api_name]['best_time_of_day'] = stats.get('best_time_of_day')
        except Exception:
            pass
    
    def save_history(self):
        """Save learning data to file"""
        try:
            data = {
                'api_stats': {},
                'session_data': self.session_data,
                'last_updated': datetime.now().isoformat()
            }
            
            for api_name, history in self.api_history.items():
                data['api_stats'][api_name] = {
                    'consecutive_fails': history['consecutive_fails'],
                    'best_time_of_day': history['best_time_of_day'],
                    'total_success': len(history['success']),
                    'total_fail': len(history['fail'])
                }
            
            with open(self.history_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception:
            pass
    
    def record_result(self, api_name: str, success: bool, response_time: float, carrier: str = None):
        """Record API result for learning"""
        timestamp = time.time()
        hour = datetime.now().hour
        
        if success:
            self.api_history[api_name]['success'].append(timestamp)
            self.api_history[api_name]['last_success_time'] = timestamp
            self.api_history[api_name]['consecutive_fails'] = 0
            self.api_history[api_name]['response_times'].append(response_time)
            
            # Learn best time of day
            if not self.api_history[api_name]['best_time_of_day']:
                self.api_history[api_name]['best_time_of_day'] = hour
            
            if carrier:
                self.api_history[api_name]['carrier_success'][carrier] += 1
        else:
            self.api_history[api_name]['fail'].append(timestamp)
            self.api_history[api_name]['last_fail_time'] = timestamp
            self.api_history[api_name]['consecutive_fails'] += 1
        
        self.session_data['total_attempts'] += 1
        if success:
            self.session_data['total_success'] += 1
    
    def predict_success_rate(self, api_name: str) -> float:
        """Predict success rate for an API using historical data"""
        history = self.api_history[api_name]
        
        # If no history, return neutral
        total = len(history['success']) + len(history['fail'])
        if total == 0:
            return 0.5
        
        # Calculate base success rate
        base_rate = len(history['success']) / total
        
        # Apply time decay - recent results matter more
        recent_window = 300  # 5 minutes
        current_time = time.time()
        
        recent_success = sum(1 for t in history['success'] if current_time - t < recent_window)
        recent_fail = sum(1 for t in history['fail'] if current_time - t < recent_window)
        recent_total = recent_success + recent_fail
        
        if recent_total > 0:
            recent_rate = recent_success / recent_total
            # Weight recent data more heavily
            predicted_rate = (base_rate * 0.3) + (recent_rate * 0.7)
        else:
            predicted_rate = base_rate
        
        # Penalize consecutive failures
        if history['consecutive_fails'] > 3:
            predicted_rate *= 0.5
        elif history['consecutive_fails'] > 5:
            predicted_rate *= 0.2
        
        # Bonus for time of day match
        current_hour = datetime.now().hour
        if history['best_time_of_day'] and abs(current_hour - history['best_time_of_day']) <= 2:
            predicted_rate *= 1.2
        
        return min(1.0, max(0.0, predicted_rate))
    
    def get_optimal_apis(self, all_apis: List[Dict], count: int = None) -> List[Dict]:
        """Get best APIs based on AI prediction"""
        if count is None:
            count = len(all_apis)
        
        # Score each API
        scored_apis = []
        for api in all_apis:
            score = self.predict_success_rate(api['name'])
            scored_apis.append((score, api))
        
        # Sort by score (highest first)
        scored_apis.sort(key=lambda x: x[0], reverse=True)
        
        # Return top N APIs
        return [api for score, api in scored_apis[:count]]
    
    def calculate_optimal_delay(self, current_success_rate: float, mode: str = 'normal') -> float:
        """Calculate optimal delay based on current performance"""
        if mode == 'turbo':
            base_delay = 0.5
        elif mode == 'stealth':
            base_delay = 5.0
        else:
            base_delay = 2.0
        
        # Adjust based on success rate
        if current_success_rate > 0.7:
            # High success - can go faster
            return base_delay * 0.7
        elif current_success_rate < 0.3:
            # Low success - slow down
            return base_delay * 1.5
        else:
            return base_delay
    
    def should_retry_api(self, api_name: str) -> bool:
        """Decide if an API should be retried"""
        history = self.api_history[api_name]
        
        # Don't retry if too many consecutive failures
        if history['consecutive_fails'] > 10:
            return False
        
        # Check if recently failed
        if history['last_fail_time']:
            time_since_fail = time.time() - history['last_fail_time']
            if time_since_fail < 60:  # Failed in last minute
                return False
        
        return True
    
    def get_smart_batch_size(self, total_apis: int, mode: str = 'normal') -> int:
        """Calculate optimal batch size"""
        if mode == 'turbo':
            return total_apis  # All at once
        elif mode == 'stealth':
            return min(5, total_apis)  # Small batches
        else:
            # Adaptive based on success rate
            if self.session_data['total_attempts'] > 0:
                success_rate = self.session_data['total_success'] / self.session_data['total_attempts']
                if success_rate > 0.6:
                    return min(15, total_apis)
                elif success_rate > 0.3:
                    return min(10, total_apis)
                else:
                    return min(5, total_apis)
            return min(10, total_apis)
    
    def analyze_patterns(self) -> Dict:
        """Analyze patterns in bombing data"""
        patterns = {
            'best_apis': [],
            'worst_apis': [],
            'best_time': None,
            'avg_response_time': 0,
            'recommendations': []
        }
        
        # Find best and worst APIs
        api_scores = []
        for api_name, history in self.api_history.items():
            total = len(history['success']) + len(history['fail'])
            if total > 0:
                success_rate = len(history['success']) / total
                api_scores.append((api_name, success_rate, total))
        
        api_scores.sort(key=lambda x: x[1], reverse=True)
        
        if api_scores:
            patterns['best_apis'] = [name for name, rate, _ in api_scores[:5]]
            patterns['worst_apis'] = [name for name, rate, _ in api_scores[-5:]]
        
        # Calculate average response time
        all_response_times = []
        for history in self.api_history.values():
            all_response_times.extend(history['response_times'])
        
        if all_response_times:
            patterns['avg_response_time'] = sum(all_response_times) / len(all_response_times)
        
        # Generate recommendations
        if self.session_data['total_attempts'] > 0:
            success_rate = self.session_data['total_success'] / self.session_data['total_attempts']
            
            if success_rate < 0.3:
                patterns['recommendations'].append("Low success rate - Try Stealth Mode")
                patterns['recommendations'].append("Consider increasing delays between waves")
            elif success_rate > 0.7:
                patterns['recommendations'].append("High success rate - Try Turbo Mode for faster bombing")
            
            if len(patterns['worst_apis']) > 10:
                patterns['recommendations'].append("Many APIs failing - Check internet connection")
        
        return patterns
    
    def get_session_stats(self) -> Dict:
        """Get current session statistics"""
        stats = {
            'total_attempts': self.session_data['total_attempts'],
            'total_success': self.session_data['total_success'],
            'success_rate': 0,
            'active_apis': 0,
            'learning_progress': 0
        }
        
        if self.session_data['total_attempts'] > 0:
            stats['success_rate'] = (self.session_data['total_success'] / 
                                    self.session_data['total_attempts']) * 100
        
        # Count active APIs (those with recent activity)
        current_time = time.time()
        for history in self.api_history.values():
            if history['last_success_time'] and (current_time - history['last_success_time']) < 300:
                stats['active_apis'] += 1
        
        # Learning progress (0-100%)
        total_data_points = sum(len(h['success']) + len(h['fail']) 
                               for h in self.api_history.values())
        stats['learning_progress'] = min(100, (total_data_points / 500) * 100)
        
        return stats


class AdaptiveDelayOptimizer:
    """Optimizes delays based on real-time performance"""
    
    def __init__(self):
        self.success_history = deque(maxlen=20)
        self.current_delay = 2.0
        self.min_delay = 0.5
        self.max_delay = 10.0
    
    def update(self, success: bool):
        """Update optimizer with result"""
        self.success_history.append(1 if success else 0)
    
    def get_optimal_delay(self) -> float:
        """Calculate optimal delay"""
        if len(self.success_history) < 5:
            return self.current_delay
        
        recent_success_rate = sum(self.success_history) / len(self.success_history)
        
        # Adjust delay based on success rate
        if recent_success_rate > 0.7:
            # High success - decrease delay
            self.current_delay *= 0.9
        elif recent_success_rate < 0.3:
            # Low success - increase delay
            self.current_delay *= 1.2
        
        # Keep within bounds
        self.current_delay = max(self.min_delay, min(self.max_delay, self.current_delay))
        
        return self.current_delay


class SmartAPISelector:
    """Intelligently selects APIs based on multiple factors"""
    
    def __init__(self, ai_engine: AIEngine):
        self.ai_engine = ai_engine
        self.carrier_map = {
            '6': 'Vodafone/Vi',
            '7': 'Airtel/Jio',
            '8': 'Airtel/BSNL',
            '9': 'Jio/Airtel'
        }
    
    def detect_carrier(self, phone: str) -> str:
        """Detect carrier from phone number"""
        if phone and len(phone) >= 1:
            return self.carrier_map.get(phone[0], 'Unknown')
        return 'Unknown'
    
    def select_best_apis(self, all_apis: List[Dict], phone: str, count: int = None) -> List[Dict]:
        """Select best APIs for given phone number"""
        carrier = self.detect_carrier(phone)
        
        # Score APIs based on carrier success
        scored_apis = []
        for api in all_apis:
            base_score = self.ai_engine.predict_success_rate(api['name'])
            
            # Bonus for carrier-specific success
            carrier_bonus = 0
            if carrier in self.ai_engine.api_history[api['name']]['carrier_success']:
                carrier_success = self.ai_engine.api_history[api['name']]['carrier_success'][carrier]
                if carrier_success > 0:
                    carrier_bonus = 0.1
            
            final_score = base_score + carrier_bonus
            scored_apis.append((final_score, api))
        
        # Sort by score
        scored_apis.sort(key=lambda x: x[0], reverse=True)
        
        # Return top N
        if count:
            return [api for score, api in scored_apis[:count]]
        return [api for score, api in scored_apis]