/**
 * SMS-POWERBOMB Desktop App v10.0
 * Electron Main Process
 */

const { app, BrowserWindow, Menu, ipcMain } = require('electron');
const path = require('path');
const Store = require('electron-store');

const store = new Store();

// Keep a global reference of the window object
let mainWindow;

function createWindow() {
  // Create the browser window
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    minWidth: 800,
    minHeight: 600,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    },
    icon: path.join(__dirname, 'icon.png'),
    backgroundColor: '#0f0f1e',
    title: 'SMS-POWERBOMB v10.0'
  });

  // Load the frontend
  const frontendUrl = store.get('frontendUrl', 'http://localhost:5173');
  mainWindow.loadURL(frontendUrl);

  // Open DevTools in development
  if (process.env.NODE_ENV === 'development') {
    mainWindow.webContents.openDevTools();
  }

  // Create application menu
  const menuTemplate = [
    {
      label: 'File',
      submenu: [
        {
          label: 'Settings',
          click: () => {
            mainWindow.webContents.send('navigate', '/settings');
          }
        },
        { type: 'separator' },
        {
          label: 'Exit',
          accelerator: 'CmdOrCtrl+Q',
          click: () => {
            app.quit();
          }
        }
      ]
    },
    {
      label: 'View',
      submenu: [
        { role: 'reload' },
        { role: 'forceReload' },
        { role: 'toggleDevTools' },
        { type: 'separator' },
        { role: 'resetZoom' },
        { role: 'zoomIn' },
        { role: 'zoomOut' },
        { type: 'separator' },
        { role: 'togglefullscreen' }
      ]
    },
    {
      label: 'Help',
      submenu: [
        {
          label: 'About',
          click: () => {
            mainWindow.webContents.send('show-about');
          }
        },
        {
          label: 'Documentation',
          click: async () => {
            const { shell } = require('electron');
            await shell.openExternal('https://github.com/RAJSARASWATI-JATAV/Sms-Bomb');
          }
        }
      ]
    }
  ];

  const menu = Menu.buildFromTemplate(menuTemplate);
  Menu.setApplicationMenu(menu);

  // Emitted when the window is closed
  mainWindow.on('closed', function () {
    mainWindow = null;
  });
}

// This method will be called when Electron has finished initialization
app.whenReady().then(() => {
  createWindow();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

// Quit when all windows are closed
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});

// IPC handlers
ipcMain.handle('get-config', () => {
  return {
    frontendUrl: store.get('frontendUrl', 'http://localhost:5173'),
    backendUrl: store.get('backendUrl', 'http://localhost:8000')
  };
});

ipcMain.handle('set-config', (event, config) => {
  if (config.frontendUrl) store.set('frontendUrl', config.frontendUrl);
  if (config.backendUrl) store.set('backendUrl', config.backendUrl);
  return true;
});

ipcMain.handle('get-version', () => {
  return app.getVersion();
});

console.log('🖥️  SMS-POWERBOMB Desktop App v10.0');
console.log('Created by: RAJSARASWATI JATAV');