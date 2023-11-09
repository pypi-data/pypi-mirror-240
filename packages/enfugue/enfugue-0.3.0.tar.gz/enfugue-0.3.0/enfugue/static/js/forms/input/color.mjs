import{View}from"../../view/base.mjs";import{ElementBuilder}from"../../base/builder.mjs";import{InputView}from"./base.mjs";import{StringInputView}from"./string.mjs";import{isEmpty,hslToHex,hslToRgb,hexToHsl}from"../../base/helpers.mjs";const E=new ElementBuilder;class ColorInputHelperView extends View{static tagName="enfugue-color-input-helper-view";constructor(t,e,s,i){super(t),this.h=isEmpty(e)?0:360*e,this.s=isEmpty(s)?1:s,this.l=isEmpty(i)?.5:i,this.changeCallbacks=[]}onChange(t){this.changeCallbacks.push(t)}get hex(){return hslToHex(this.h/360,this.s,this.l)}get rgb(){return hslToRgb(this.h/360,this.s,this.l)}get hsl(){return[this.h/360,this.s,this.l]}set hex(t){if(!isEmpty(t))try{let[e,s,i]=hexToHsl(t);this.h=360*e,this.s=s,this.l=i}catch(e){console.warn("Couldn't parse hexadecimal value",t)}this.checkUpdateNode()}set hue(t){this.h=t,this.checkUpdateNode()}get hue(){return this.h}set saturation(t){this.s=t,this.checkUpdateNode()}get saturation(){return 100*this.s+"%"}set lightness(t){this.l=t,this.checkUpdateNode()}get lightness(){return 100*this.l+"%"}get hueBackground(){return`linear-gradient(to right, ${new Array(360).fill(null).map(((t,e)=>`hsl(${e}, 100%, 50%)`)).join(", ")})`}get saturationBackground(){return`linear-gradient(to right, ${new Array(100).fill(null).map(((t,e)=>`hsl(${this.hue}, ${e}%, 50%)`)).join(", ")})`}get lightnessBackground(){return`linear-gradient(to right, ${new Array(100).fill(null).map(((t,e)=>`hsl(${this.hue}, ${this.saturation}, ${e}%)`)).join(", ")})`}async checkUpdateNode(){if(void 0!==this.node){let t=this.node.findAll(".input-part"),e=t.map((t=>t.find(".indicator"))),[s,i,n]=t,[h,r,l]=e,o=this.node.find(".preview");h.css("left",this.h/360*100+"%"),r.css("left",100*this.s+"%"),l.css("left",100*this.l+"%"),s.css("background-image",this.hueBackground),i.css("background-image",this.saturationBackground),n.css("background-image",this.lightnessBackground),o.css("background-color",this.hex)}}async changed(){for(let t of this.changeCallbacks)await t(this.hex)}async build(){let t=await super.build(),e=E.div().class("indicator"),s=E.div().class("input-part").content(e),i=E.div().class("indicator"),n=E.div().class("input-part").content(i),h=E.div().class("indicator"),r=E.div().class("input-part").content(h),l=E.div().class("input-container").content(s,n,r),o=E.div().class("preview"),a=E.div().class("preview-input-container").content(o,l);t.on("mouseenter",(t=>{this.within=!0})).on("mouseleave",(e=>{this.within=!1,this.hideOnLeave&&(this.hideOnLeave=!1,t.hide())})),e.css("left",this.h/360+"$"),i.css("left",100*this.s+"%"),h.css("left",100*this.l+"%"),s.css("background-image",this.hueBackground),n.css("background-image",this.saturationBackground),r.css("background-image",this.lightnessBackground),o.css("background-color",this.hex).content(E.div().css("color","white").content("Preview"),E.div().css("color","black").content("Preview"));let u=(t,e,s)=>{let i,n=e=>{let s=t.element.getBoundingClientRect();return(e.clientX-s.x)/s.width},h=t=>{t=Math.max(0,Math.min(t,1)),s(t,i),i=t,this.checkUpdateNode(),this.changed()};t.on("mousedown",(e=>{h(n(e)),t.on("mousemove",(t=>{h(n(t))})).on("mouseup,mouseleave",(e=>{e.preventDefault(),e.stopPropagation(),h(n(e)),t.off("mouseup,mouseleave,mousemove")}))})).on("click",(t=>{t.preventDefault(),t.stopPropagation()}))};return u(s,0,(t=>{this.h=Math.round(360*t)})),u(n,0,(t=>{this.s=t})),u(r,0,(t=>{this.l=t})),t.content(a)}}class ColorInputView extends InputView{static tagName="enfugue-color-input";static stringInputClass=StringInputView;static defaultValue="#ff0000";constructor(t,e,s){super(t,e,s),this.stringInput=new this.constructor.stringInputClass(t,"hex",{value:this.value});let[i,n,h]=hexToHsl(this.value);this.colorInputHelper=new ColorInputHelperView(t,i,n,h),this.colorInputHelper.onChange((t=>{this.stringInput.setValue(t,!1),this.value=t,this.changed()})),this.stringInput.onFocus((async()=>{if(!this.disabled){await this.stringInput.getNode();let t=await this.colorInputHelper.getNode(),e=this.node.element.getBoundingClientRect(),s=e.x,i=e.y+e.height,n=e.width,h=(e,h,r)=>{s=e,i=h,n=r,t.css({width:`${r}px`,left:`${e}px`,top:`${h}px`})};this.repositionInterval=setInterval((()=>{e=this.node.element.getBoundingClientRect();let t=e.x,r=e.y+e.height,l=e.width;s===t&&i===r&&n===l||h(t,r,l)}),25),document.body.appendChild(t.render()),h(s,i,n),t.css({width:`${e.width}px`,left:`${e.x}px`,top:`${e.y+e.height}px`});let r=strip(this.stringInput.getValue());r.match(/^#[abcdefABCDEF0-9]{6}$/)&&(this.colorInputHelper.hex=r,this.value=r),this.colorInputHelper.show();let l=t=>{this.colorInputHelper.hide(),window.removeEventListener("click",l,!1),clearInterval(this.repositionInterval)};window.addEventListener("click",l,!1)}})),this.stringInput.onInput((async()=>{let t=this.stringInput.getValue();t.match(/^#[abcdefABCDEF0-9]{6}$/)&&(this.colorInputHelper.hex=t,this.value=t,this.changed())})),this.stringInput.onBlur((async t=>{let e=strip(this.stringInput.getValue());e.match(/^#[abcdefABCDEF0-9]{6}$/)?(this.colorInputHelper.hex=e,this.value=e,this.changed()):(this.value=this.colorInputHelper.hex,this.stringInput.setValue(this.value,!1),this.changed()),this.colorInputHelper.within?this.colorInputHelper.hideOnLeave=!0:this.colorInputHelper.hide()}))}disable(){super.disable(),this.stringInput.disable()}enable(){super.enable(),this.stringInput.enable()}getValue(){return this.value}setValue(t,e){super.setValue(t,!1);void 0!==this.stringInput&&this.stringInput.setValue(t,!1),void 0!==this.colorInputHelper&&(this.colorInputHelper.hex=t),e&&this.changed()}changed(){if(void 0!==this.node){let t=this.node.find(".inline-color-preview");t&&t.css("background-color",this.value)}super.changed()}async build(){let t=await super.build();return t.append(E.span().class("inline-color-preview").css("background-color",this.value).on("click",(()=>{this.stringInput.focus()})),await this.stringInput.getNode()),t}}export{ColorInputView};
