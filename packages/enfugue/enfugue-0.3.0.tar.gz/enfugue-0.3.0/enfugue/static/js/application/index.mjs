import{getQueryParameters,getDataParameters,downloadAsBlob,createEvent,waitFor,isEmpty,merge,sleep}from"../base/helpers.mjs";import{Session}from"../base/session.mjs";import{Publisher}from"../base/publisher.mjs";import{TooltipHelper}from"../common/tooltip.mjs";import{MenuView,SidebarView}from"../view/menu.mjs";import{StatusView}from"../view/status.mjs";import{NotificationCenterView}from"../view/notifications.mjs";import{WindowsView}from"../nodes/windows.mjs";import{ImageView,BackgroundImageView}from"../view/image.mjs";import{VideoView,VideoPlayerView}from"../view/video.mjs";import{Model}from"../model/enfugue.mjs";import{View}from"../view/base.mjs";import{ControlsHelperView}from"../view/controls.mjs";import{FileNameFormView}from"../forms/enfugue/files.mjs";import{StringInputView}from"../forms/input.mjs";import{InvocationController}from"../controller/common/invocation.mjs";import{SamplesController}from"../controller/common/samples.mjs";import{ModelPickerController}from"../controller/common/model-picker.mjs";import{ModelManagerController}from"../controller/common/model-manager.mjs";import{DownloadsController}from"../controller/common/downloads.mjs";import{LayersController}from"../controller/common/layers.mjs";import{PromptTravelController}from"../controller/common/prompts.mjs";import{AnimationsController}from"../controller/common/animations.mjs";import{AnnouncementsController}from"../controller/common/announcements.mjs";import{HistoryDatabase}from"../common/history.mjs";import{SimpleNotification}from"../common/notify.mjs";import{CheckpointInputView,LoraInputView,LycorisInputView,InversionInputView,ModelPickerInputView,DefaultVaeInputView,MotionModuleInputView}from"../forms/input.mjs";import{ConfirmFormView,YesNoFormView}from"../forms/confirm.mjs";import{ImageEditorView,ImageEditorNodeView,ImageEditorImageNodeView}from"../nodes/image-editor.mjs";class LogoutButtonView extends View{static tagName="i";static className="fa-solid fa-right-from-bracket logout";async logout(){window.location="/logout"}async build(){let t=await super.build();return t.on("click",(()=>this.logout())),t.data("tooltip","Logout"),t}}class Application{static menuCategories={file:"File"};static adminMenuCategories={models:"Models",system:"System"};static menuCategoryShortcuts={file:"f",models:"m",system:"s",help:"h"};static filenameFormInputWidth=400;static filenameFormInputHeight=250;static logoShadowRGB=[0,0,0];static logoShadowOpacity=.5;static logoShadowSteps=10;static logoShadowOffset=2;static logoShadowSpread=0;static confirmViewWidth=500;static confirmViewHeight=200;constructor(t){isEmpty(window.enfugue)||isEmpty(window.enfugue.config)||(t=merge(t,window.enfugue.config)),this.config=t,this.publisher=new Publisher}async initialize(){this.tooltips=new TooltipHelper,this.container=document.querySelector(this.config.view.applicationContainer),isEmpty(this.container)?console.error(`Couldn't find application configuration using selector ${this.config.view.applicationContainer}, abandoning initialization.`):(this.container.classList.add("loader"),this.container.classList.add("loading"),this.session=Session.getScope("enfugue",2592e6),this.model=new Model(this.config),this.menu=new MenuView(this.config),this.sidebar=new SidebarView(this.config),this.windows=new WindowsView(this.config),this.notifications=new NotificationCenterView(this.config),this.history=new HistoryDatabase(this.config.history.size,this.config.debug),this.images=new ImageEditorView(this),this.controlsHelper=new ControlsHelperView(this.config),this.container.appendChild(await this.menu.render()),this.container.appendChild(await this.sidebar.render()),this.container.appendChild(await this.images.render()),this.container.appendChild(await this.windows.render()),this.container.appendChild(await this.notifications.render()),this.container.appendChild(await this.controlsHelper.render()),this.config.debug&&console.log("Starting animations."),await this.startAnimations(),this.config.debug&&console.log("Registering dynamic inputs."),await this.registerDynamicInputs(),this.config.debug&&console.log("Registering download controllers."),await this.registerDownloadsControllers(),this.config.debug&&console.log("Registering animation controllers."),await this.registerAnimationsControllers(),this.config.debug&&console.log("Registering model controllers."),await this.registerModelControllers(),this.config.debug&&console.log("Registering invocation controllers."),await this.registerInvocationControllers(),this.config.debug&&console.log("Registering sample controllers."),await this.registerSampleControllers(),this.config.debug&&console.log("Registering layer controllers."),await this.registerLayersControllers(),this.config.debug&&console.log("Registering prompt controllers."),await this.registerPromptControllers(),this.config.debug&&console.log("Registering menu controllers."),await this.registerMenuControllers(),this.config.debug&&console.log("Registering sidebar controllers."),await this.registerSidebarControllers(),this.config.debug&&console.log("Starting autosave."),await this.startAutosave(),this.config.debug&&console.log("Starting announcement check."),await this.startAnnouncements(),this.config.debug&&console.log("Starting keepalive."),await this.startKeepalive(),this.config.debug&&console.log("Registering authentication."),await this.registerLogout(),window.onpopstate=t=>this.popState(t),document.addEventListener("dragover",(t=>this.onDragOver(t))),document.addEventListener("drop",(t=>this.onDrop(t))),document.addEventListener("paste",(t=>this.onPaste(t))),document.addEventListener("keypress",(t=>this.onKeyPress(t))),document.addEventListener("keyup",(t=>this.onKeyUp(t))),document.addEventListener("keydown",(t=>this.onKeyDown(t))),this.config.debug&&console.log("Application initialization complete."),this.publish("applicationReady"),this.container.classList.remove("loading"))}async startAnnouncements(){this.userIsAdmin&&!this.userIsSandboxed&&(this.announcements=new AnnouncementsController(this),await this.announcements.initialize())}async startAnimations(){let t=document.querySelector("header h1");isEmpty(t)?console.warn("Can't find header logo, not binding animations."):(this.animations=!0,window.addEventListener("mousemove",(e=>{if(!1===this.animations)return;let[i,o]=[e.clientX/window.innerWidth,e.clientY/window.innerHeight],s=[];for(let t=0;t<this.constructor.logoShadowSteps;t++){let[e,n]=[i*(t+1)*this.constructor.logoShadowOffset,o*(t+1)*this.constructor.logoShadowOffset],a=this.constructor.logoShadowOpacity-t/this.constructor.logoShadowSteps*this.constructor.logoShadowOpacity,r=`rgba(${this.constructor.logoShadowRGB.concat(a.toFixed(2)).join(",")})`;s.push(`${e}px ${n}px ${this.constructor.logoShadowSpread}px ${r}`)}t.style.textShadow=s.join(",")})))}async enableAnimations(){this.animations||(this.animations=!0,this.session.setItem("animations",!0),document.body.classList.remove("no-animations"),this.publish("animationsEnabled"))}async disableAnimations(){this.animations&&(this.animations=!1,this.session.setItem("animations",!1),document.body.classList.add("no-animations"),this.publish("animationsDisabled"))}async registerDynamicInputs(){this.userIsAdmin||delete DefaultVaeInputView.defaultOptions.other,CheckpointInputView.defaultOptions=async()=>(await this.model.get("/checkpoints")).reduce(((t,e)=>(isEmpty(e.directory)||"."===e.directory?t[e.name]=e.name:t[e.name]=`<strong>${e.name}</strong><span class='note' style='margin-left: 2px'>(${e.directory})</note>`,t)),{}),LoraInputView.defaultOptions=async()=>(await this.model.get("/lora")).reduce(((t,e)=>(isEmpty(e.directory)||"."===e.directory?t[e.name]=e.name:t[e.name]=`<strong>${e.name}</strong><span class='note' style='margin-left: 2px'>(${e.directory})</note>`,t)),{}),LycorisInputView.defaultOptions=async()=>(await this.model.get("/lycoris")).reduce(((t,e)=>(isEmpty(e.directory)||"."===e.directory?t[e.name]=e.name:t[e.name]=`<strong>${e.name}</strong><span class='note' style='margin-left: 2px'>(${e.directory})</note>`,t)),{}),InversionInputView.defaultOptions=async()=>(await this.model.get("/inversions")).reduce(((t,e)=>(isEmpty(e.directory)||"."===e.directory?t[e.name]=e.name:t[e.name]=`<strong>${e.name}</strong><span class='note' style='margin-left: 2px'>(${e.directory})</note>`,t)),{}),MotionModuleInputView.defaultOptions=async()=>(await this.model.get("/motion")).reduce(((t,e)=>(isEmpty(e.directory)||"."===e.directory?t[e.name]=e.name:t[e.name]=`<strong>${e.name}</strong><span class='note' style='margin-left: 2px'>(${e.directory})</note>`,t)),{}),ModelPickerInputView.defaultOptions=async()=>(await this.model.get("/model-options")).reduce(((t,e)=>{let i=isEmpty(e.type)?"":"checkpoint"===e.type?"Checkpoint":"checkpoint+diffusers"===e.type?"Checkpoint + Diffusers Cache":"diffusers"===e.type?"Diffusers Cache":"Preconfigured Model";return isEmpty(e.directory)||"."===e.directory?t[`${e.type}/${e.name}`]=`<strong>${e.name}</strong><em>${i}</em>`:t[`${e.type}/${e.name}`]=`<strong>${e.name}</strong><span class='note' style='margin-left: 2px'>(${e.directory})</note></span><em>${i}</em>`,t}),{})}async registerModelControllers(){this.modelManager=new ModelManagerController(this),await this.modelManager.initialize(),this.modelPicker=new ModelPickerController(this),await this.modelPicker.initialize()}async registerDownloadsControllers(){this.downloads=new DownloadsController(this),await this.downloads.initialize()}async registerInvocationControllers(){this.engine=new InvocationController(this),await this.engine.initialize()}async registerSampleControllers(){this.samples=new SamplesController(this),await this.samples.initialize()}async registerLayersControllers(){this.layers=new LayersController(this),await this.layers.initialize()}async registerPromptControllers(){this.prompts=new PromptTravelController(this),await this.prompts.initialize()}async registerAnimationsControllers(){this.animation=new AnimationsController(this),await this.animation.initialize()}get userIsAdmin(){return!isEmpty(window.enfugue)&&!0===window.enfugue.admin}get userIsSandboxed(){return!isEmpty(window.enfugue)&&!0===window.enfugue.sandboxed}getMenuCategories(){let t={...this.constructor.menuCategories};return this.userIsAdmin&&(t={...t,...this.constructor.adminMenuCategories},this.userIsSandboxed&&delete t.system),t.help="Help",t}async registerMenuControllers(){let t=this.getMenuCategories();this.menuControllers={};for(let e in t){let i=t[e],o=this.constructor.menuCategoryShortcuts[e];this.menuControllers[e]=[];try{let t=await import(`../controller/${e}/index.autogenerated.mjs`),s=await this.menu.addCategory(i,o);for(let i of t.Index)try{let t=(await import(`../controller/${e}/${i}`)).MenuController;if(isEmpty(t))throw"Module does not provide a 'MenuController' export.";if(!t.isDisabled()){let i=await s.addItem(t.menuName,t.menuIcon,t.menuShortcut),o=new t(this);await o.initialize(),i.onClick((()=>o.onClick())),this.menuControllers[e].push(o)}}catch(t){console.warn("Couldn't import",e,"menu controller",i,t)}}catch(t){console.warn("Couldn't register controllers for menu",e,t)}}}async registerSidebarControllers(){let t=await import("../controller/sidebar/index.autogenerated.mjs");this.sidebarControllers=[];for(let e of t.Index){let t=(await import(`../controller/sidebar/${e}`)).SidebarController;if(isEmpty(t))throw"Module does not provide a 'SidebarController' export.";let i=new t(this);await i.initialize(),this.sidebarControllers.push(i)}}async startKeepalive(){const t=this.config.model.status.interval||1e4,e=t=>{"ready"===t?this.publish("engineReady"):"busy"===t?this.publish("engineBusy"):"idle"===t?this.publish("engineIdle"):console.warn("Unknown status",t)};let i=document.querySelector("header");if(isEmpty(i))return void console.warn("No header found on page, not appending status view.");let o=await this.model.get(),s=new StatusView(this.config,o),n=await s.getNode();!isEmpty(o.system)&&!isEmpty(o.system.downloads)&&o.system.downloads.active>0&&this.downloads.checkStartTimer(),e(o.status),i.appendChild(n.render()),setInterval((async()=>{try{let t=await this.model.get();o.status!==t.status&&e(t.status),!isEmpty(o.system)&&!isEmpty(o.system.downloads)&&o.system.downloads.active>0&&this.downloads.checkStartTimer(),s.updateStatus(t),o=t}catch{s.updateStatus("error")}}),t);let a=await this.model.get("/invocation"),r=null;for(let t of a)if("processing"===t.status){r=t;break}isEmpty(r)||(isEmpty(r)||isEmpty(r.metadata)||isEmpty(r.metadata.tensorrt_build)?(this.notifications.push("info","Active Invocation Found","You have an image currently being generated, beginning monitoring process."),this.engine.canvasInvocation(r.uuid)):this.notifications.push("info","TensorRT Build in Progress",`You have a TensorRT engine build in progress for ${r.metadata.tensorrt_build.model}. You'll receive a notification in this window when it is complete. The engine will remain unavailable until that time.`),this.publish("invocationBegin",r)),setInterval((async()=>{try{let t,e=await this.model.get("/invocation");for(let i of e)"processing"===i.status&&(null!==r&&r.id===i.id||(t=i)),isEmpty(r)||i.id!==r.id||i.status===r.status||("completed"===i.status?this.publish("invocationComplete",i):this.publish("invocationError",i),r=null);isEmpty(t)||(this.publish("invocationBegin",t),r=t)}catch(t){console.error(t)}}),t)}async registerLogout(){if(!isEmpty(window.enfugue.user)&&"noauth"!==window.enfugue.user){let t=new LogoutButtonView(this.config);document.querySelector("header").appendChild((await t.getNode()).render())}}async startAutosave(){try{let t=await this.history.getCurrentState();if(!isEmpty(t)&&(this.config.debug&&console.log("Loading autosaved state",t),await this.setState(t),this.notifications.push("info","Session Restored","Your last autosaved session was successfully loaded."),!isEmpty(this.images.node))){let t=this.images.node.find("enfugue-node-editor-zoom-reset");isEmpty(t)||t.trigger("click")}const e=this.config.model.autosave.interval||3e4;setInterval((()=>this.autosave()),e)}catch(t){console.error(t),this.notifications.push("warn","History Disabled","Couldn't open IndexedDB, history and autosave are disabled.")}}async autosave(t=!0){try{await this.history.setCurrentState(this.getState()),t&&SimpleNotification.notify("Session autosaved!",2e3)}catch(t){console.error("Couldn't autosave",t)}}subscribe(t,e){this.publisher.subscribe(t,e)}unsubscribe(t,e){this.publisher.unsubscribe(t,e)}async publish(t,e=null){this.publisher.publish(t,e)}spawnConfirmForm(t,e,i,o=!0,s=!1){return new Promise((async(n,a)=>{let r,l=!1,m=new t(this.config,i);m.onSubmit((()=>{l=!0,n(!0),o&&r.remove()})),m.onCancel((()=>{l=!0,n(!1),r.remove()})),r=await this.windows.spawnWindow(e,m,this.constructor.confirmViewWidth,this.constructor.confirmViewHeight),r.onClose((()=>{!l&&s?a():n(!1),l=!0}))}))}spawnVideoPlayer(t,e="Video"){return new Promise((async(i,o)=>{let s=new VideoPlayerView(this.config,t);await s.waitForLoad(),i(await this.windows.spawnWindow(e,s,s.width+4,s.height+34))}))}confirm(t,e=!0){return this.spawnConfirmForm(ConfirmFormView,"Confirm",t,e)}yesNo(t,e=!0){return this.spawnConfirmForm(YesNoFormView,"Yes or No",t,e,!0)}async saveAs(t,e,i,o){let s=new Blob([e],{type:i});return this.saveBlobAs(t,s,o)}async saveRemoteAs(t,e){let i=e.split("/").slice(-1)[0].split(".")[1];return this.saveBlobAs(t,await downloadAsBlob(e),i)}async saveBlobAs(t,e,i){i.startsWith(".")||(i=`.${i}`);let o=window.URL.createObjectURL(e),s=new FileNameFormView(this.config),n=await this.windows.spawnWindow(t,s,this.constructor.filenameFormInputWidth,this.constructor.filenameFormInputHeight);s.onCancel((()=>n.close())),s.onSubmit((t=>{let e=t.filename;e.endsWith(i)&&(e=e.substring(0,e.length-i.length));let s=document.createElement("a");s.setAttribute("download",`${e}${i}`),s.href=o,document.body.appendChild(s),window.requestAnimationFrame((()=>{s.dispatchEvent(createEvent("click")),document.body.removeChild(s),n.remove()}))})),n.onClose((()=>window.URL.revokeObjectURL(o)))}async onPaste(t){let e=(t.clipboardData||t.originalEvent.clipboardData).items;for(let t of e)"file"===t.kind?this.loadFile(t.getAsFile()):t.getAsString((t=>this.onTextPaste(t)))}getStateFromMetadata(t){return isEmpty(t.EnfugueUIState)?{}:JSON.parse(t.EnfugueUIState)}async loadFile(t,e="Image"){let i=new FileReader;i.addEventListener("load",(async()=>{let t,e=i.result.substring(5,i.result.indexOf(";")),o=e.length+13;switch(e){case"application/json":await this.setState(JSON.parse(atob(i.result.substring(o)))),this.notifications.push("info","Generation Settings Loaded","Image generation settings were successfully retrieved from image metadata.");break;case"image/png":t=new BackgroundImageView(this.config,i.result),await t.waitForLoad();let s=this.getStateFromMetadata(t.metadata);if(!isEmpty(s)&&await this.yesNo("It looks like this image was made with Enfugue. Would you like to load the identified generation settings?"))return await this.setState(s),void this.notifications.push("info","Generation Settings Loaded","Image generation settings were successfully retrieved from image metadata.");case"image/gif":case"image/avif":case"image/jpeg":case"image/bmp":case"image/tiff":case"image/x-icon":case"image/webp":isEmpty(t)&&(t=new BackgroundImageView(this.config,i.result,!1)),this.samples.showCanvas(),this.layers.addImageLayer(t);break;case"video/mp4":this.samples.showCanvas(),this.layers.addVideoLayer(i.result);break;default:this.notifications.push("warn","Unhandled File Type",`File type "${e}" is not handled by Enfugue.`)}})),i.readAsDataURL(t)}async onTextPaste(t){t.startsWith("<html>")}getStatefulControllers(){let t=[this.modelPicker,this.layers,this.samples,this.prompts].concat(this.sidebarControllers);for(let e in this.menuControllers)t=t.concat(this.menuControllers[e]);return t}getState(t=!0){let e={},i=this.getStatefulControllers();for(let o of i)e={...e,...o.getState(t)};return e}shouldSaveState(){let t=this.getState();return!(isEmpty(t.prompts)||isEmpty(t.prompts.prompt)&&isEmpty(t.prompts.negativePrompt))||!isEmpty(t.layers)}async setState(t,e=!1){!0===e&&this.shouldSaveState()&&(await this.autosave(!1),await this.history.flush(t));let i=this.getStatefulControllers();isEmpty(t.canvas)||this.images.setDimension(t.canvas.width,t.canvas.height);for(let e of i)await e.setState(t)}async resetState(t=!0){let e={layers:[]},i=this.getStatefulControllers();for(let t of i)e={...e,...t.getDefaultState()};await this.setState(e,t),this.images.resetCanvasPosition()}async initializeStateFromImage(t,e=!0,i=null,o=null,s=!1){try{let n,a={},r=this.getStatefulControllers();null===i&&(i=await this.yesNo("Would you like to keep settings?<br /><br />This will maintain things like prompts and other global settings the same while only changing the dimensions to match the image."));for(let t of r)a=i?{...a,...t.getState()}:{...a,...t.getDefaultState()};if(a.layers=[],a.samples={urls:null,video:null,active:null,animation:!1},!isEmpty(o))for(let t in o)void 0!==a[t]&&(null===o[t]?a[t]=null:"object"==typeof a[t]&&"object"==typeof o[t]?a[t]={...a[t],...o[t]}:a[t]=o[t]);this.samples.showCanvas(),await sleep(1),await this.setState(a,e),await sleep(1),n=s?await this.layers.addVideoLayer(t):await this.layers.addImageLayer(t),await sleep(1),await n.editorNode.scaleCanvasToSize()}catch(t){console.error(t)}}invoke(t){return t.state=this.getState(!1),this.engine.invoke(t)}onKeyPress(t){t.shiftKey&&(this.menu.fireCategoryShortcut(t.key),this.publish("keyboardShortcut",t.key))}onKeyDown(t){"Shift"===t.key&&this.menu.addClass("highlight")}onKeyUp(t){"Shift"===t.key&&this.menu.removeClass("highlight")}onDragOver(t){t.preventDefault()}onDrop(t){t.preventDefault(),t.stopPropagation();try{this.loadFile(t.dataTransfer.files[0])}catch(t){console.warn(t)}}async popState(t){}}export{Application};
