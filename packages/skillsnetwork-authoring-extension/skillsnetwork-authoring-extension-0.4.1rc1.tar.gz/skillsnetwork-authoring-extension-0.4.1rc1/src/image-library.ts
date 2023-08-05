import { Widget } from '@lumino/widgets';
import { Dialog } from '@jupyterlab/apputils';
import { Globals, IMAGE_LIBRARY_URL } from './config';

export class ImageLibraryWidget extends Widget {
    constructor() {
      const body = document.createElement('iframe');
      body.src = `${IMAGE_LIBRARY_URL}?atlas_token=${Globals.TOKEN}`
      body.setAttribute("frameborder", "0")
      body.setAttribute("allow", "clipboard-read; clipboard-write")
      super({ node: body });
    }
}

export class ImageLibrary {
    launch(){
        const imgLibDialog = new Dialog({title: "Image Library",
        body:  new ImageLibraryWidget(),
        hasClose: true,
        buttons: []
        });
        const dialogContent = imgLibDialog.node.querySelector(".jp-Dialog-content")
        if (dialogContent){
        dialogContent.classList.add("image-library-dialog");
        }
        imgLibDialog.launch()
    }
}
