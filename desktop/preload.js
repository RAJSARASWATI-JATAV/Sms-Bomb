/**
 * Preload script for Electron
 * Exposes safe APIs to the renderer process
 */

const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  getConfig: () => ipcRenderer.invoke('get-config'),
  setConfig: (config) => ipcRenderer.invoke('set-config', config),
  getVersion: () => ipcRenderer.invoke('get-version'),
  onNavigate: (callback) => ipcRenderer.on('navigate', callback),
  onShowAbout: (callback) => ipcRenderer.on('show-about', callback)
});