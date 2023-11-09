import{View,ParentView}from"./base.mjs";import{ElementBuilder}from"../base/builder.mjs";import{isEmpty}from"../base/helpers.mjs";const E=new ElementBuilder;class ScribbleView extends View{static tagName="enfugue-scribble-view";static defaultPencilSize=6;static maximumPencilSize=100;static defaultPencilShape="circle";constructor(e,t,i,s=!0){super(e),this.width=t,this.height=i,this.active=!1,this.invert=s,this.shape=this.constructor.defaultPencilShape,this.size=this.constructor.defaultPencilSize,this.isEraser=!1,this.memoryCanvas=document.createElement("canvas"),this.visibleCanvas=document.createElement("canvas"),this.onDrawCallbacks=[],isEmpty(t)||isEmpty(i)||(this.memoryCanvas.width=t,this.memoryCanvas.height=i,this.visibleCanvas.width=t,this.visibleCanvas.height=i)}get activeColor(){return this.invert?"white":"black"}get backgroundColor(){return this.invert?"black":"white"}onDraw(e){this.onDrawCallbacks.push(e)}drawn(){for(let e of this.onDrawCallbacks)e()}get src(){return this.updateVisibleCanvas(),this.visibleCanvas.toDataURL()}get invertSrc(){let e=document.createElement("canvas");e.width=this.visibleCanvas.width,e.height=this.visibleCanvas.height;let t=e.getContext("2d");return t.drawImage(this.visibleCanvas,0,0),t.globalCompositeOperation="difference",t.fillStyle="white",t.fillRect(0,0,e.width,e.height),e.toDataURL()}clearMemory(){let e=this.memoryCanvas.getContext("2d");e.fillStyle=this.backgroundColor,e.fillRect(0,0,this.memoryCanvas.width,this.memoryCanvas.height),this.updateVisibleCanvas(),this.drawn()}fillMemory(){let e=this.memoryCanvas.getContext("2d");e.fillStyle=this.activeColor,e.fillRect(0,0,this.memoryCanvas.width,this.memoryCanvas.height),this.updateVisibleCanvas(),this.drawn()}invertMemory(){this.setMemory(this.invertSrc)}setMemory(e){let t=document.createElement("canvas");t.width=e.width,t.height=e.height,this.visibleCanvas.width=t.width,this.visibleCanvas.height=t.height,t.getContext("2d").drawImage(e,0,0),this.memoryCanvas=t,this.updateVisibleCanvas(),this.drawn()}resizeCanvas(e,t){if(this.width=e,this.height=t,this.visibleCanvas.width=e,this.visibleCanvas.height=t,e>this.memoryCanvas.width||t>this.memoryCanvas.height){let i=document.createElement("canvas");i.width=e,i.height=t;let s=i.getContext("2d");s.fillStyle=this.backgroundColor,s.fillRect(0,0,e,t),s.drawImage(this.memoryCanvas,0,0),this.memoryCanvas=i}this.updateVisibleCanvas(),this.drawn()}updateVisibleCanvas(){let e=this.visibleCanvas.getContext("2d");e.beginPath(),e.rect(0,0,this.width,this.height),e.fillStyle=this.backgroundColor,e.fill(),e.drawImage(this.memoryCanvas,0,0)}getCoordinates(e){return[e.offsetX,e.offsetY]}onNodeMouseEnter(e){this.active=!1}onNodeMouseLeave(e){this.active=!1,this.updateVisibleCanvas(),this.lastX=null,this.lastY=null}onNodeMouseDown(e){if(1!==e.which||e.metaKey||e.ctrlKey)return;e.preventDefault(),e.stopPropagation(),this.active=!0;let[t,i]=this.getCoordinates(e);isEmpty(this.lastX)||isEmpty(this.lastY)||!e.shiftKey||this.drawLineTo(t,i),e.altKey||this.isEraser?this.erase(t,i):this.drawMemory(t,i)}onNodeMouseUp(e){this.active=!1}onNodeMouseMove(e){let[t,i]=this.getCoordinates(e);if(!isEmpty(this.lastDrawTime)&&!e.altKey&&!this.isEraser){(new Date).getTime()-this.lastDrawTime<50&&this.drawLineTo(t,i)}this.active?(e.preventDefault(),e.stopPropagation(),e.altKey||this.isEraser?this.erase(t,i):this.drawMemory(t,i)):this.drawVisible(t,i)}decreaseSize(){this.size=Math.max(2,this.size-2)}increaseSize(){this.size=Math.min(this.constructor.maximumPencilSize,this.size+2)}onNodeWheel(e){if(e.ctrlKey||e.metaKey)return void e.preventDefault();e.deltaY>0?this.decreaseSize():this.increaseSize();let[t,i]=this.getCoordinates(e);this.drawVisible(t,i),e.preventDefault(),e.stopPropagation()}erase(e,t){let i=this.memoryCanvas.getContext("2d");i.save(),this.drawPencilShape(i,e,t),i.clip(),i.fillStyle=this.backgroundColor,i.fillRect(0,0,this.memoryCanvas.width,this.memoryCanvas.height),i.restore(),this.updateVisibleCanvas(),this.drawn()}drawMemory(e,t){let i=this.memoryCanvas.getContext("2d");this.drawPencilShape(i,e,t),i.fillStyle=this.activeColor,i.fill(),this.updateVisibleCanvas(),this.lastX=e,this.lastY=t,this.lastDrawTime=(new Date).getTime(),this.drawn()}drawVisible(e,t){this.updateVisibleCanvas();let i=this.visibleCanvas.getContext("2d");this.size-=1,this.drawPencilShape(i,e,t),i.strokeStyle=this.backgroundColor,i.lineWidth=1,i.stroke(),this.size+=1,this.drawPencilShape(i,e,t),i.strokeStyle=this.activeColor,i.lineWidth=1,i.stroke()}drawLineTo(e,t){let i=this.memoryCanvas.getContext("2d");i.beginPath(),i.moveTo(this.lastX,this.lastY),i.lineTo(e,t),i.strokeStyle=this.activeColor,i.lineWidth=this.size,i.stroke(),this.drawn()}drawPencilShape(e,t,i){if(e.beginPath(),"circle"===this.shape)e.arc(t,i,this.size/2,0,2*Math.PI);else{let s=Math.max(0,t-this.size/2),a=Math.max(0,i-this.size/2),h=Math.min(s+this.size,this.width),o=Math.min(a+this.size,this.height);e.moveTo(s,a),e.lineTo(h,a),e.lineTo(h,o),e.lineTo(s,o),e.lineTo(s,a)}}async build(){let e=await super.build();return e.append(this.visibleCanvas),e.on("dblclick",(e=>{e.preventDefault(),e.stopPropagation()})),e.on("mouseenter",(e=>this.onNodeMouseEnter(e))),e.on("mousemove",(e=>this.onNodeMouseMove(e))),e.on("mousedown",(e=>this.onNodeMouseDown(e))),e.on("mouseup",(e=>this.onNodeMouseUp(e))),e.on("mouseleave",(e=>this.onNodeMouseLeave(e))),e.on("wheel",(e=>this.onNodeWheel(e))),this.updateVisibleCanvas(),e}}export{ScribbleView};
