import{isEmpty}from"../../base/helpers.mjs";import{ElementBuilder}from"../../base/builder.mjs";import{Controller}from"../base.mjs";import{View}from"../../view/base.mjs";import{ImageView}from"../../view/image.mjs";import{ToolbarView}from"../../view/menu.mjs";import{ImageEditorScribbleNodeOptionsFormView,ImageEditorPromptNodeOptionsFormView,ImageEditorImageNodeOptionsFormView,ImageEditorVideoNodeOptionsFormView}from"../../forms/enfugue/image-editor.mjs";const E=new ElementBuilder;class LayerOptionsView extends View{static tagName="enfugue-layer-options-view";static placeholderText="No options available. When you select a layer with options, they will appear in this pane.";async setForm(e){this.node.content(await e.getNode())}async resetForm(){this.node.content(E.div().class("placeholder").content(this.constructor.placeholderText))}async build(){let e=await super.build();return e.content(E.div().class("placeholder").content(this.constructor.placeholderText)),e}}class LayersView extends View{static tagName="enfugue-layers-view";static placeholderText="No layers yet. Use the buttons above to add layers, drag and drop videos or images onto the canvas, or paste media from your clipboard.";constructor(e){super(e),this.toolbar=new ToolbarView(e)}async emptyLayers(){this.node.content(await this.toolbar.getNode(),E.div().class("placeholder").content(this.constructor.placeholderText))}async addLayer(e,t=!1){t?this.node.content(await this.toolbar.getNode(),await e.getNode()):(this.node.append(await e.getNode()),this.node.render())}async build(){let e=await super.build();return e.content(await this.toolbar.getNode(),E.div().class("placeholder").content(this.constructor.placeholderText)),e.on("drop",(e=>{e.preventDefault(),e.stopPropagation()})),e}}class LayerView extends View{static previewWidth=30;static previewHeight=30;static tagName="enfugue-layer-view";constructor(e,t,i){super(e.config),this.controller=e,this.editorNode=t,this.form=i,this.isActive=!1,this.isVisible=!0,this.isLocked=!1,this.previewImage=new ImageView(e.config,null,!1),this.editorNode.onResize((()=>this.resized())),this.getLayerImage().then((e=>this.previewImage.setImage(e))),this.form.onSubmit((()=>{setTimeout((()=>{this.drawPreviewImage()}),150)})),this.subtitle=null}get foregroundStyle(){return window.getComputedStyle(document.documentElement).getPropertyValue("--theme-color-primary")}async getLayerImage(){let e=this.controller.images.width,t=this.controller.images.height,i=Math.max(e,t),a=this.constructor.previewWidth/i,s=e/i,o=t/i,r=this.constructor.previewWidth*s,l=this.constructor.previewHeight*o,d=this.editorNode.getState(!0),n=d.x*a,h=d.y*a,c=d.w*a,g=d.h*a,m=document.createElement("canvas");this.lastCanvasWidth=e,this.lastCanvasHeight=t,this.lastNodeWidth=d.w,this.lastNodeHeight=d.h,this.lastNodeX=d.x,this.lastNodeY=d.y,m.width=r,m.height=l;let y=m.getContext("2d");if(d.src){let e=d.src;if(e.startsWith("data:video")||e.endsWith("mp4")||e.endsWith("webp")||e.endsWith("avi")||e.endsWith("mov")){let t=document.createElement("canvas");t.width=this.editorNode.content.video.videoWidth,t.height=this.editorNode.content.video.videoHeight,t.getContext("2d").drawImage(this.editorNode.content.video,0,0),e=t.toDataURL()}let t=new ImageView(this.config,e);await t.waitForLoad();let i=0,s=0,o=t.width*a,r=t.height*a,l=isEmpty(d.anchor)?null:d.anchor.split("-");if("cover"===d.fit||"contain"===d.fit){let e=c/t.width,a=g/t.height;if("cover"===d.fit){let d=Math.ceil(t.width*e),n=Math.ceil(t.height*e),h=Math.ceil(t.width*a),m=Math.ceil(t.height*a);if(c<=d&&g<=n){if(o=d,r=n,!isEmpty(l))switch(l[0]){case"center":i=Math.floor(g/2-r/2);break;case"bottom":i=g-r}}else if(c<=h&&g<=m&&(o=h,r=m,!isEmpty(l)))switch(l[1]){case"center":s=Math.floor(c/2-o/2);break;case"right":s=c-o}}else{let d=Math.floor(t.width*e),n=Math.floor(t.height*e),h=Math.floor(t.width*a),m=Math.floor(t.height*a);if(c>=d&&g>=n){if(o=d,r=n,!isEmpty(l))switch(l[0]){case"center":i=Math.floor(g/2-r/2);break;case"bottom":i=g-r}}else if(c>=h&&g>=m&&(o=h,r=m,!isEmpty(l)))switch(l[1]){case"center":s=Math.floor(c/2-o/2);break;case"right":s=c-o}}}else if("stretch"===d.fit)o=c,r=g;else if(!isEmpty(l)){switch(l[0]){case"center":i=Math.floor(g/2-r/2);break;case"bottom":i=g-r}switch(l[1]){case"center":s=Math.floor(c/2-o/2);break;case"right":s=c-o}}y.beginPath(),y.rect(n,h,c,g),y.clip(),y.drawImage(t.image,n+s,h+i,o,r)}else y.fillStyle=this.foregroundStyle,y.fillRect(n,h,c,g);return m.toDataURL()}async resized(){let e=this.controller.images.width,t=this.controller.images.height,i=this.editorNode.getState();e===this.lastCanvasWidth&&t===this.lastCanvasHeight&&i.w===this.lastNodeWidth&&i.h===this.lastNodeHeight&&i.x===this.lastNodeX&&i.y===this.lastNodeY||this.drawPreviewImage()}async drawPreviewImage(){this.previewImage.setImage(await this.getLayerImage())}async remove(){this.controller.removeLayer(this)}async setActive(e){this.isActive=e,this.isActive?this.addClass("active"):this.removeClass("active")}async setVisible(e){if(this.isVisible=e,!isEmpty(this.hideShowLayer)){let e=this.isVisible?"fa-solid fa-eye":"fa-solid fa-eye-slash";this.hideShowLayer.setIcon(e)}this.isVisible?this.editorNode.show():this.editorNode.hide()}async setLocked(e){if(this.isLocked=e,!isEmpty(this.lockUnlockLayer)){let e=this.isLocked?"fa-solid fa-lock":"fa-solid fa-lock-open";this.lockUnlockLayer.setIcon(e)}this.isLocked?this.editorNode.addClass("locked"):this.editorNode.removeClass("locked")}getState(e=!0){return{...this.editorNode.getState(e),...this.form.values,isLocked:this.isLocked,isActive:this.isActive,isVisible:this.isVisible}}async setState(e){await this.editorNode.setState(e),await this.form.setValues(e)}async setName(e){void 0!==this.node&&this.node.find("span.name").content(e)}async setSubtitle(e){if(this.subtitle=e,void 0!==this.node){let t=this.node.find("span.subtitle");isEmpty(e)?t.empty().hide():t.content(e).show()}}async build(){let e=await super.build();this.toolbar=new ToolbarView(this.config);let t=this.isVisible?"Hide Layer":"Show Layer",i=this.isVisible?"fa-solid fa-eye":"fa-solid fa-eye-slash";this.hideShowLayer=await this.toolbar.addItem(t,i);this.isLocked,this.isLocked;this.lockUnlockLayer=await this.toolbar.addItem("Lock Layer","fa-solid fa-lock-open"),this.hideShowLayer.onClick((()=>this.setVisible(!this.isVisible))),this.lockUnlockLayer.onClick((()=>this.setLocked(!this.isLocked)));let a=E.span().class("name").content(this.editorNode.name),s=E.span().class("subtitle");return isEmpty(this.subtitle)?s.hide():s.content(this.subtitle),e.content(await this.hideShowLayer.getNode(),await this.lockUnlockLayer.getNode(),E.div().class("title").content(a,s),await this.previewImage.getNode(),E.button().content("&times;").class("close").on("click",(()=>this.remove()))).attr("draggable","true").on("dragstart",(e=>{e.dataTransfer.effectAllowed="move",this.controller.draggedLayer=this,this.addClass("dragging")})).on("dragleave",(e=>{this.removeClass("drag-target-below").removeClass("drag-target-above"),this.controller.dragTarget===this&&(this.controller.dragTarget=null)})).on("dragover",(e=>{if(this.controller.draggedLayer!==this){let t=e.layerY>e.target.getBoundingClientRect().height/2;t?this.removeClass("drag-target-above").addClass("drag-target-below"):this.addClass("drag-target-above").removeClass("drag-target-below"),this.controller.dragTarget=this,this.controller.dropBelow=t}})).on("dragend",(e=>{this.controller.dragEnd(),this.removeClass("dragging").removeClass("drag-target-below").removeClass("drag-target-above"),e.preventDefault(),e.stopPropagation()})).on("click",(e=>{this.controller.activate(this)})).on("drop",(e=>{e.preventDefault(),e.stopPropagation()})),e}}class LayersController extends Controller{removeLayer(e,t=!0){t&&e.editorNode.remove(!1);let i=this.layers.indexOf(e);-1!==i?(this.layers=this.layers.slice(0,i).concat(this.layers.slice(i+1)),0===this.layers.length?(this.layersView.emptyLayers(),this.layerOptions.resetForm()):this.layersView.node.remove(e.node.element),e.isActive&&this.layerOptions.resetForm(),this.layersChanged()):console.error("Couldn't find",e)}dragEnd(){if(!isEmpty(this.draggedLayer)&&!isEmpty(this.dragTarget)&&this.draggedLayer!==this.dragTarget){this.draggedLayer.removeClass("dragging"),this.dragTarget.removeClass("drag-target-above").removeClass("drag-target-below");let e=this.layers.indexOf(this.draggedLayer),t=this.layers.indexOf(this.dragTarget);t>e&&t--,this.dropBelow||t++,t!==e&&(this.images.reorderNode(t,this.draggedLayer.editorNode),this.layers=this.layers.filter((e=>e!==this.draggedLayer)),this.layers.splice(t,0,this.draggedLayer),this.layersView.node.remove(this.draggedLayer.node),this.layersView.node.insert(t+1,this.draggedLayer.node),this.layersView.node.render(),this.layersChanged())}this.draggedLayer=null,this.dragTarget=null}getState(e=!0){return{layers:this.layers.map((t=>t.getState(e)))}}getDefaultState(){return{layers:[]}}async setState(e){if(this.emptyLayers(),!isEmpty(e.layers)){for(let t of e.layers)await this.addLayerByState(t);this.activateLayer(this.layers.length-1)}}async addLayerByState(e,t=null){let i;switch(e.classname){case"ImageEditorPromptNodeView":i=await this.addPromptLayer(!1,t,e.name);break;case"ImageEditorScribbleNodeView":i=await this.addScribbleLayer(!1,t,e.name);break;case"ImageEditorImageNodeView":i=await this.addImageLayer(e.src,!1,t,e.name);break;case"ImageEditorVideoNodeView":i=await this.addVideoLayer(e.src,!1,t,e.name);break;default:console.error(`Unknown layer class ${e.classname}, skipping and dumping layer data.`),console.log(e),console.log(t)}return isEmpty(i)||await i.setState(e),i}async emptyLayers(){for(let e of this.layers)this.images.removeNode(e.editorNode);this.layers=[],this.layersView.emptyLayers(),this.layerOptions.resetForm(),this.layersChanged()}async activateLayer(e){if(-1!==e){for(let t=0;t<this.layers.length;t++)this.layers[t].setActive(t===e);this.layerOptions.setForm(this.layers[e].form)}}activate(e){return this.activateLayer(this.layers.indexOf(e))}async addLayer(e,t=!0){e.editorNode.onNameChange((t=>{e.setName(t,!1)})),e.editorNode.onClose((()=>{this.removeLayer(e,!1)})),e.form.onSubmit((()=>{this.layersChanged()})),this.layers.push(e),await this.layersView.addLayer(e,1===this.layers.length),t&&this.activateLayer(this.layers.length-1),this.layersChanged()}async addVideoLayer(e,t=!0,i=null,a="Video"){isEmpty(i)&&(i=await this.images.addVideoNode(e,a));let s=new ImageEditorVideoNodeOptionsFormView(this.config),o=new LayerView(this,i,s);return s.onSubmit((e=>{let t=[];if(e.denoise&&t.push("Video to Video"),e.videoPrompt&&t.push("Prompt"),e.control&&!isEmpty(e.controlnetUnits)){let i=e.controlnetUnits.map((e=>isEmpty(e.controlnet)?"canny":e.controlnet)),a=i.filter(((e,t)=>i.indexOf(e)===t));t.push(`ControlNet (${a.join(", ")})`)}let a=isEmpty(t)?"Passthrough":t.join(", ");i.updateOptions(e),o.setSubtitle(a)})),await this.addLayer(o,t),o}async addImageLayer(e,t=!0,i=null,a="Image"){e instanceof ImageView&&(e=e.src),isEmpty(i)&&(i=await this.images.addImageNode(e,a));let s=new ImageEditorImageNodeOptionsFormView(this.config),o=new LayerView(this,i,s);return s.onSubmit((e=>{let t=[];if(e.denoise&&t.push("Image to Image"),e.imagePrompt&&t.push("Prompt"),e.control&&!isEmpty(e.controlnetUnits)){let i=e.controlnetUnits.map((e=>isEmpty(e.controlnet)?"canny":e.controlnet)),a=i.filter(((e,t)=>i.indexOf(e)===t));t.push(`ControlNet (${a.join(", ")})`)}let a=isEmpty(t)?"Passthrough":t.join(", ");i.updateOptions(e),o.setSubtitle(a)})),await this.addLayer(o,t),o}async addScribbleLayer(e=!0,t=null,i="Scribble"){isEmpty(t)&&(t=await this.images.addScribbleNode(i));let a,s=new ImageEditorScribbleNodeOptionsFormView(this.config),o=new LayerView(this,t,s);return t.content.onDraw((()=>{this.activate(o),clearTimeout(a),a=setTimeout((()=>{o.drawPreviewImage()}),100)})),await this.addLayer(o,e),o}async addPromptLayer(e=!0,t=null,i="Prompt"){isEmpty(t)&&(t=await this.images.addPromptNode(i));let a=new ImageEditorPromptNodeOptionsFormView(this.config),s=new LayerView(this,t,a);return a.onSubmit((e=>{t.setPrompts(e.prompt,e.negativePrompt)})),await this.addLayer(s,e),s}async promptAddImageLayer(){let e;try{e=await promptFiles()}catch(e){}isEmpty(e)||this.application.loadFile(e,truncate(e.name,16))}getLayerByEditorNode(e){return this.layers.filter((t=>t.editorNode===e)).shift()}async addCopiedNode(e,t){let i=this.getLayerByEditorNode(t).getState(),a=e.getState();await this.addLayerByState({...i,...a},e),this.activateLayer(this.layers.length-1)}async layersChanged(){this.publish("layersChanged",this.getState().layers)}async initialize(){this.layers=[],this.layerOptions=new LayerOptionsView(this.config),this.layersView=new LayersView(this.config);let e=await this.layersView.toolbar.addItem("Image/Video","fa-regular fa-image"),t=await this.layersView.toolbar.addItem("Draw Scribble","fa-solid fa-pencil");e.onClick((()=>this.promptAddImageLayer())),t.onClick((()=>this.addScribbleLayer())),this.application.container.appendChild(await this.layerOptions.render()),this.application.container.appendChild(await this.layersView.render()),this.images.onNodeFocus((e=>{this.activate(this.getLayerByEditorNode(e))})),this.images.onNodeCopy(((e,t)=>{this.addCopiedNode(e,t)}))}}export{LayersController};
