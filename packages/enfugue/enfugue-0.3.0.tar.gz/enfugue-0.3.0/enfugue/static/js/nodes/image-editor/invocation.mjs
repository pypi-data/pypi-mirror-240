import{SimpleNotification}from"../../common/notify.mjs";import{isEmpty}from"../../base/helpers.mjs";import{View}from"../../view/base.mjs";import{ImageView}from"../../view/image.mjs";import{ToolbarView}from"../../view/menu.mjs";import{UpscaleFormView,DownscaleFormView}from"../../forms/enfugue/upscale.mjs";import{ImageAdjustmentView,ImageFilterView}from"./filter.mjs";class InvocationToolbarView extends ToolbarView{constructor(i){super(i.config),this.invocationNode=i}async onMouseEnter(i){this.invocationNode.toolbarEntered()}async onMouseLeave(i){this.invocationNode.toolbarLeft()}async build(){let i=await super.build();return i.on("mouseenter",(i=>this.onMouseEnter(i))),i.on("mouseleave",(i=>this.onMouseLeave(i))),i}}class CurrentInvocationImageView extends View{constructor(i){super(i.config),this.editor=i,this.imageView=new ImageView(this.config)}static className="current-invocation-image-view";static hideTime=250;static imageAdjustmentWindowWidth=750;static imageAdjustmentWindowHeight=525;static imageFilterWindowWidth=450;static imageFilterWindowHeight=350;static imageUpscaleWindowWidth=300;static imageUpscaleWindowHeight=320;static imageDownscaleWindowWidth=260;static imageDownscaleWindowHeight=210;async getTools(){return isEmpty(this.toolbar)&&(this.toolbar=new InvocationToolbarView(this),this.hideImage=await this.toolbar.addItem("Hide Image","fa-solid fa-eye-slash"),this.hideImage.onClick((()=>this.editor.application.images.hideCurrentInvocation())),navigator.clipboard&&"function"==typeof ClipboardItem&&(this.copyImage=await this.toolbar.addItem("Copy to Clipboard","fa-solid fa-clipboard"),this.copyImage.onClick((()=>this.copyToClipboard()))),this.popoutImage=await this.toolbar.addItem("Popout Image","fa-solid fa-arrow-up-right-from-square"),this.popoutImage.onClick((()=>this.sendToWindow())),this.saveImage=await this.toolbar.addItem("Save As","fa-solid fa-floppy-disk"),this.saveImage.onClick((()=>this.saveToDisk())),this.adjustImage=await this.toolbar.addItem("Adjust Image","fa-solid fa-sliders"),this.adjustImage.onClick((()=>this.startImageAdjustment())),this.filterImage=await this.toolbar.addItem("Filter Image","fa-solid fa-wand-magic-sparkles"),this.filterImage.onClick((()=>this.startImageFilter())),this.editImage=await this.toolbar.addItem("Edit Image","fa-solid fa-pen-to-square"),this.editImage.onClick((()=>this.sendToCanvas())),this.upscaleImage=await this.toolbar.addItem("Upscale Image","fa-solid fa-up-right-and-down-left-from-center"),this.upscaleImage.onClick((()=>this.startImageUpscale())),this.downscaleImage=await this.toolbar.addItem("Downscale Image","fa-solid fa-down-left-and-up-right-to-center"),this.downscaleImage.onClick((()=>this.startImageDownscale()))),this.toolbar}async prepareMenu(i){if((await i.addItem("Hide Image","fa-solid fa-eye-slash","d")).onClick((()=>this.editor.application.images.hideCurrentInvocation())),navigator.clipboard&&"function"==typeof ClipboardItem){(await i.addItem("Copy to Clipboard","fa-solid fa-clipboard","c")).onClick((()=>this.copyToClipboard()))}(await i.addItem("Popout Image","fa-solid fa-arrow-up-right-from-square","p")).onClick((()=>this.sendToWindow())),(await i.addItem("Save As","fa-solid fa-floppy-disk","a")).onClick((()=>this.saveToDisk())),(await i.addItem("Adjust Image","fa-solid fa-sliders","j")).onClick((()=>this.startImageAdjustment())),(await i.addItem("Filter Image","fa-solid fa-wand-magic-sparkles","l")).onClick((()=>this.startImageFilter())),(await i.addItem("Edit Image","fa-solid fa-pen-to-square","t")).onClick((()=>this.sendToCanvas())),(await i.addItem("Upscale Image","fa-solid fa-up-right-and-down-left-from-center","u")).onClick((()=>this.startImageUpscale())),(await i.addItem("Downscale Image","fa-solid fa-down-left-and-up-right-to-center","w")).onClick((()=>this.startImageDownscale()))}setImage(i){this.imageView.setImage(i),isEmpty(this.imageAdjuster)||this.imageAdjuster.setImage(i)}async waitForLoad(){await this.imageView.waitForLoad()}async copyToClipboard(){navigator.clipboard.write([new ClipboardItem({"image/png":await this.imageView.getBlob()})]),SimpleNotification.notify("Copied to clipboard!",2e3)}async saveToDisk(){this.editor.application.saveBlobAs("Save Image",await this.imageView.getBlob(),".png")}async sendToCanvas(){this.editor.application.initializeStateFromImage(await this.imageView.getImageAsDataURL(),!0,null,{samples:null})}async startImageDownscale(){if(this.checkActiveTool("downscale"))return;let i=this.imageView.src,e=this.imageView.width,t=this.imageView.height,a=async e=>{let t=new ImageView(this.config,i);await t.waitForLoad(),await t.downscale(e),this.imageView.setImage(t.src),this.editor.setDimension(t.width,t.height,!1)},s=!1;this.imageDownscaleForm=new DownscaleFormView(this.config),this.imageDownscaleWindow=await this.editor.application.windows.spawnWindow("Downscale Image",this.imageDownscaleForm,this.constructor.imageDownscaleWindowWidth,this.constructor.imageDownscaleWindowHeight),this.imageDownscaleWindow.onClose((()=>{this.imageDownscaleForm=null,this.imageDownscaleWindow=null,s||(this.imageView.setImage(i),this.editor.setDimension(e,t,!1))})),this.imageDownscaleForm.onChange((async()=>a(this.imageDownscaleForm.values.downscale))),this.imageDownscaleForm.onCancel((()=>this.imageDownscaleWindow.remove())),this.imageDownscaleForm.onSubmit((async i=>{s=!0,this.imageDownscaleWindow.remove()})),a(2)}async startImageUpscale(){this.checkActiveTool("upscale")||(this.imageUpscaleForm=new UpscaleFormView(this.config),this.imageUpscaleWindow=await this.editor.application.windows.spawnWindow("Upscale Image",this.imageUpscaleForm,this.constructor.imageUpscaleWindowWidth,this.constructor.imageUpscaleWindowHeight),this.imageUpscaleWindow.onClose((()=>{this.imageUpscaleForm=null,this.imageUpscaleWindow=null})),this.imageUpscaleForm.onCancel((()=>this.imageUpscaleWindow.remove())),this.imageUpscaleForm.onSubmit((async i=>{await this.editor.application.initializeStateFromImage(await this.imageView.getImageAsDataURL(),!0,!0,{upscale:[i],generation:{samples:1,iterations:1},samples:null}),this.imageUpscaleWindow.remove(),this.editor.application.images.hideCurrentInvocation(),setTimeout((()=>{this.editor.application.publish("tryInvoke")}),2e3)})))}async startImageFilter(){if(this.checkActiveTool("filter"))return;this.imageFilterView=new ImageFilterView(this.config,this.imageView.src,this.node.element.parentElement),this.imageFilterWindow=await this.editor.application.windows.spawnWindow("Filter Image",this.imageFilterView,this.constructor.imageFilterWindowWidth,this.constructor.imageFilterWindowHeight);let i=()=>{try{this.imageFilterView.removeCanvas()}catch(i){}this.imageFilterView=null,this.imageFilterWindow=null};this.imageFilterWindow.onClose(i),this.imageFilterView.onSave((async()=>{this.imageView.setImage(this.imageFilterView.getImageSource()),setTimeout((()=>{this.imageFilterWindow.remove(),i()}),150)})),this.imageFilterView.onCancel((()=>{this.imageFilterWindow.remove(),i()}))}async startImageAdjustment(){if(this.checkActiveTool("adjust"))return;this.imageAdjustmentView=new ImageAdjustmentView(this.config,this.imageView.src,this.node.element.parentElement),this.imageAdjustmentWindow=await this.editor.application.windows.spawnWindow("Adjust Image",this.imageAdjustmentView,this.constructor.imageAdjustmentWindowWidth,this.constructor.imageAdjustmentWindowHeight);let i=()=>{try{this.imageAdjustmentView.removeCanvas()}catch(i){}this.imageAdjustmentView=null,this.imageAdjustmentWindow=null};this.imageAdjustmentWindow.onClose(i),this.imageAdjustmentView.onSave((async()=>{this.imageView.setImage(this.imageAdjustmentView.getImageSource()),await this.waitForLoad(),setTimeout((()=>{this.imageAdjustmentWindow.remove(),i()}),150)})),this.imageAdjustmentView.onCancel((()=>{this.imageAdjustmentWindow.remove(),i()}))}checkActiveTool(i){return isEmpty(this.imageAdjustmentWindow)?isEmpty(this.imageFilterWindow)?isEmpty(this.imageUpscaleWindow)?!isEmpty(this.imagedownscaleWindow)&&("downscale"!==i?this.editor.application.notifications.push("warn","Finish Downscaling",`Complete your downscale selection or cancel before trying to ${i}.`):this.imagedownscaleWindow.focus(),!0):("upscale"!==i?this.editor.application.notifications.push("warn","Finish Upscaling",`Complete your upscale selection or cancel before trying to ${i}.`):this.imageUpscaleWindow.focus(),!0):("filter"!==i?this.editor.application.notifications.push("warn","Finish Filtering",`Complete filtering before trying to ${i}.`):this.imageFilterWindow.focus(),!0):("adjust"!==i?this.editor.application.notifications.push("warn","Finish Adjusting",`Complete adjustments before trying to ${i}.`):this.imageAdjustmentWindow.focus(),!0)}async sendToWindow(){const i=URL.createObjectURL(await this.getBlob());window.open(i,"_blank")}async toolbarEntered(){this.stopHideTimer()}async toolbarLeft(){this.startHideTimer()}stopHideTimer(){clearTimeout(this.timer)}startHideTimer(){this.timer=setTimeout((async()=>{let i=await this.lock.acquire(),e=await this.getTools();this.node.element.parentElement.removeChild(await e.render()),i()}),this.constructor.hideTime)}async onMouseEnter(i){this.stopHideTimer();let e=await this.lock.acquire(),t=await this.getTools();this.node.element.parentElement.appendChild(await t.render()),e()}async onMouseLeave(i){this.startHideTimer()}async build(){let i=await super.build();return i.content(await this.imageView.getNode()),i.on("mouseenter",(i=>this.onMouseEnter(i))),i.on("mouseleave",(i=>this.onMouseLeave(i))),i}}export{InvocationToolbarView,CurrentInvocationImageView};
