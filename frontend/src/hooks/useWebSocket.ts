/**
 * useWebSocket Hook - Phase 5
 * React hook for WebSocket functionality
 */

import { useEffect, useState, useCallback, useRef } from 'react';
import wsClient, { type WebSocketMessage, type MessageHandler } from '../lib/websocket';

export function useWebSocket() {
  const [isConnected, setIsConnected] = useState(false);
  const [lastMessage, setLastMessage] = useState<WebSocketMessage | null>(null);
  const handlersRef = useRef<Map<string, MessageHandler>>(new Map());

  useEffect(() => {
    // Check connection status periodically
    const interval = setInterval(() => {
      setIsConnected(wsClient.isConnected());
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  const connect = useCallback(async (token: string) => {
    try {
      await wsClient.connect(token);
      setIsConnected(true);
    } catch (error) {
      console.error('Failed to connect WebSocket:', error);
      setIsConnected(false);
    }
  }, []);

  const disconnect = useCallback(() => {
    wsClient.disconnect();
    setIsConnected(false);
  }, []);

  const subscribeToCampaign = useCallback((campaignId: number) => {
    wsClient.subscribeToCampaign(campaignId);
  }, []);

  const unsubscribeFromCampaign = useCallback((campaignId: number) => {
    wsClient.unsubscribeFromCampaign(campaignId);
  }, []);

  const on = useCallback((messageType: string, handler: MessageHandler) => {
    const unsubscribe = wsClient.on(messageType, (message) => {
      setLastMessage(message);
      handler(message);
    });

    handlersRef.current.set(messageType, handler);

    return unsubscribe;
  }, []);

  useEffect(() => {
    // Cleanup handlers on unmount
    return () => {
      handlersRef.current.clear();
    };
  }, []);

  return {
    isConnected,
    lastMessage,
    connect,
    disconnect,
    subscribeToCampaign,
    unsubscribeFromCampaign,
    on,
  };
}

export function useCampaignUpdates(campaignId: number | null) {
  const [progress, setProgress] = useState<any>(null);
  const [status, setStatus] = useState<string>('');
  const { isConnected, subscribeToCampaign, unsubscribeFromCampaign, on } = useWebSocket();

  useEffect(() => {
    if (!campaignId || !isConnected) return;

    // Subscribe to campaign
    subscribeToCampaign(campaignId);

    // Register handlers
    const unsubscribeProgress = on('campaign_progress', (message) => {
      if (message.campaign_id === campaignId) {
        setProgress(message.data);
      }
    });

    const unsubscribeStarted = on('campaign_started', (message) => {
      if (message.campaign_id === campaignId) {
        setStatus('running');
      }
    });

    const unsubscribeCompleted = on('campaign_completed', (message) => {
      if (message.campaign_id === campaignId) {
        setStatus('completed');
        setProgress(message.data);
      }
    });

    const unsubscribeFailed = on('campaign_failed', (message) => {
      if (message.campaign_id === campaignId) {
        setStatus('failed');
      }
    });

    // Cleanup
    return () => {
      unsubscribeFromCampaign(campaignId);
      unsubscribeProgress();
      unsubscribeStarted();
      unsubscribeCompleted();
      unsubscribeFailed();
    };
  }, [campaignId, isConnected, subscribeToCampaign, unsubscribeFromCampaign, on]);

  return { progress, status };
}