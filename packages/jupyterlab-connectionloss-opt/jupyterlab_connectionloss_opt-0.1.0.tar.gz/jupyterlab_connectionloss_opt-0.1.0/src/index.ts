import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { ISettingRegistry } from '@jupyterlab/settingregistry';

import {IConnectionLost}  from '@jupyterlab/application';
import {ConnectionLost} from './connectionLost';

/**
 * Initialization data for the connection-opt extension.
 */
const plugin: JupyterFrontEndPlugin<IConnectionLost> = {
  id: 'connection-opt:plugin',
  autoStart: true,
  provides: IConnectionLost,
  activate: (app: JupyterFrontEnd, settingRegistry: ISettingRegistry | null) => {
    console.log('JupyterLab extension connection-opt is activated!');

    return ConnectionLost;
  }
};

export default plugin;
