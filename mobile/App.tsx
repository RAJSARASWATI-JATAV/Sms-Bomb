/**
 * SMS-POWERBOMB Mobile App v10.0
 * Main Application Component
 */

import React from 'react';
import {
  SafeAreaView,
  StatusBar,
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  ScrollView,
} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

// Home Screen
function HomeScreen({ navigation }: any) {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor="#1a1a2e" />
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.header}>
          <Text style={styles.title}>SMS-POWERBOMB</Text>
          <Text style={styles.version}>v10.0 ULTIMATE</Text>
        </View>

        <View style={styles.card}>
          <Text style={styles.cardTitle}>🔥 Quick Actions</Text>
          
          <TouchableOpacity
            style={[styles.button, styles.primaryButton]}
            onPress={() => navigation.navigate('Bomb')}>
            <Text style={styles.buttonText}>🚀 Start Bombing</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.button, styles.secondaryButton]}
            onPress={() => navigation.navigate('History')}>
            <Text style={styles.buttonText}>📊 View History</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.button, styles.secondaryButton]}
            onPress={() => navigation.navigate('Stats')}>
            <Text style={styles.buttonText}>📈 Statistics</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.card}>
          <Text style={styles.cardTitle}>ℹ️ About</Text>
          <Text style={styles.infoText}>
            SMS-POWERBOMB v10.0 Ultimate Edition
          </Text>
          <Text style={styles.infoText}>
            Created by: RAJSARASWATI JATAV
          </Text>
          <Text style={styles.infoText}>
            Team: RAJSARASWATI JATAV CYBER CREW
          </Text>
        </View>

        <View style={styles.disclaimer}>
          <Text style={styles.disclaimerText}>
            ⚠️ For educational purposes only. Use responsibly!
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

// Bomb Screen
function BombScreen() {
  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.card}>
          <Text style={styles.cardTitle}>🎯 Start SMS Bombing</Text>
          <Text style={styles.infoText}>
            Feature coming soon...
          </Text>
          <Text style={styles.infoText}>
            Connect to backend API to start bombing campaigns.
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

// History Screen
function HistoryScreen() {
  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.card}>
          <Text style={styles.cardTitle}>📊 Campaign History</Text>
          <Text style={styles.infoText}>
            No campaigns yet.
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

// Stats Screen
function StatsScreen() {
  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.card}>
          <Text style={styles.cardTitle}>📈 Statistics</Text>
          <View style={styles.statRow}>
            <Text style={styles.statLabel}>Total Campaigns:</Text>
            <Text style={styles.statValue}>0</Text>
          </View>
          <View style={styles.statRow}>
            <Text style={styles.statLabel}>Success Rate:</Text>
            <Text style={styles.statValue}>0%</Text>
          </View>
          <View style={styles.statRow}>
            <Text style={styles.statLabel}>Total SMS:</Text>
            <Text style={styles.statValue}>0</Text>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

// Main App
export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        screenOptions={{
          headerStyle: {
            backgroundColor: '#1a1a2e',
          },
          headerTintColor: '#00ff88',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}>
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: 'SMS-POWERBOMB' }}
        />
        <Stack.Screen
          name="Bomb"
          component={BombScreen}
          options={{ title: 'Start Bombing' }}
        />
        <Stack.Screen
          name="History"
          component={HistoryScreen}
          options={{ title: 'Campaign History' }}
        />
        <Stack.Screen
          name="Stats"
          component={StatsScreen}
          options={{ title: 'Statistics' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f0f1e',
  },
  scrollContent: {
    padding: 16,
  },
  header: {
    alignItems: 'center',
    marginBottom: 24,
    paddingVertical: 20,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#00ff88',
    marginBottom: 8,
  },
  version: {
    fontSize: 14,
    color: '#ff00ff',
    fontWeight: '600',
  },
  card: {
    backgroundColor: '#1a1a2e',
    borderRadius: 12,
    padding: 20,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#00ff88',
  },
  cardTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#00ff88',
    marginBottom: 16,
  },
  button: {
    padding: 16,
    borderRadius: 8,
    marginBottom: 12,
    alignItems: 'center',
  },
  primaryButton: {
    backgroundColor: '#00ff88',
  },
  secondaryButton: {
    backgroundColor: '#ff00ff',
  },
  buttonText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#0f0f1e',
  },
  infoText: {
    fontSize: 14,
    color: '#ffffff',
    marginBottom: 8,
  },
  disclaimer: {
    backgroundColor: '#ff4444',
    borderRadius: 8,
    padding: 16,
    marginTop: 8,
  },
  disclaimerText: {
    fontSize: 12,
    color: '#ffffff',
    textAlign: 'center',
    fontWeight: '600',
  },
  statRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#2a2a3e',
  },
  statLabel: {
    fontSize: 16,
    color: '#ffffff',
  },
  statValue: {
    fontSize: 16,
    color: '#00ff88',
    fontWeight: 'bold',
  },
});