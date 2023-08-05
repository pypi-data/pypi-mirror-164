/* eslint-disable prettier/prettier */
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
/* eslint-disable @typescript-eslint/ban-types */
import { DocumentRegistry } from '@jupyterlab/docregistry';
import { IDocumentManager } from '@jupyterlab/docmanager';
import { Dialog, ToolbarButton } from '@jupyterlab/apputils';
import { IDisposable, DisposableDelegate } from '@lumino/disposable';
import { IMainMenu } from '@jupyterlab/mainmenu';
import { getFileContents, getLabFilePath, loadLabContents, parseJwt } from '../tools';
import { axiosHandler, postLabModel, getLabModel } from '../handler';
import { showFailureImportLabDialog } from '../dialog';
import { Globals } from '../config';
import * as nbformat from '@jupyterlab/nbformat';
import { ATLAS_TOKEN, SET_DEFAULT_LAB_NAME_AND_KERNEL, MODE } from '../config';

import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import {
  NotebookPanel,
  INotebookModel,
  INotebookTracker
} from '@jupyterlab/notebook';

import { ImageLibrary } from '../image-library';

/**
 * The plugin registration information.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  activate,
  id: 'skillsnetwork-authoring-extension:plugin',
  autoStart: true,
  requires: [INotebookTracker, IDocumentManager, IMainMenu]
};

/**
 * A notebook widget extension that adds a button to the toolbar.
 */
export class ButtonExtension
  implements DocumentRegistry.IWidgetExtension<NotebookPanel, INotebookModel>
{
  /**
   * Create a new extension for the notebook panel widget.
   *
   * @param panel Notebook panel
   * @param context Notebook context
   * @returns Disposable on the added button
   */
  createNew(
    panel: NotebookPanel,
    context: DocumentRegistry.IContext<INotebookModel>
  ): IDisposable {
    const start = async () => {
      // Get the current file contents
      const file = await getFileContents(panel, context);
      // POST to Atlas the file contents/lab model
      postLabModel(axiosHandler(Globals.TOKEN), file);
    };

    const publishButton = new ToolbarButton({
      className: 'publish-lab-button',
      label: 'Publish',
      onClick: start,
      tooltip: 'Publish Lab'
    });

    const imageLibraryButton = new ToolbarButton({
      className: 'image-library-button',
      label: 'Image Library',
      onClick: () =>  (new ImageLibrary()).launch(),
      tooltip: 'Open Image Library'
    });

    panel.toolbar.insertItem(9, 'image-library', imageLibraryButton);
    panel.toolbar.insertItem(10, 'publish', publishButton);
    return new DisposableDelegate(() => {
      publishButton.dispose();
      imageLibraryButton.dispose();
    });
  }
}

/**
 * Activate the extension.
 *
 * @param app Main application object
 */
async function activate(
  app: JupyterFrontEnd,
  mainMenu: IMainMenu,
  docManager: IDocumentManager
) {

  console.log("Activated skillsnetwork-authoring-extension button plugin!");

  if (await MODE() == "learn") return

  // init the token
  const token = await ATLAS_TOKEN();

  //init globals
  const env_type = await SET_DEFAULT_LAB_NAME_AND_KERNEL()

  console.log('Using default kernel: ', Globals.PY_KERNEL_NAME);

  // Add the Publish widget to the lab environment
  app.docRegistry.addWidgetExtension('Notebook', new ButtonExtension());

  // Only try to load up a notebook when author is using the browser tool (not in local)
  if (token !== 'NO_TOKEN' && env_type !== "local"){    
    try{
      const parsedToken = parseJwt(token)
      const labFilename = getLabFilePath(parsedToken);
      let notebook_content = await getLabModel(axiosHandler(token)) as unknown as nbformat.INotebookContent
      // Attempt to open the lab
      const nbPanel = docManager.createNew(labFilename, 'notebook', { name:  Globals.PY_KERNEL_NAME} ) as NotebookPanel;
      if (nbPanel === undefined) {
        throw Error('Error loading lab')
      }
      loadLabContents(nbPanel, notebook_content);
      nbPanel.show();
      
    }
    catch (e){
      Dialog.flush() // remove spinner
      showFailureImportLabDialog();
      Globals.TOKEN = "NO_TOKEN";
      console.log(e)
    }
  }
}

/**
 * Export the plugin as default.
 */
export default plugin;
