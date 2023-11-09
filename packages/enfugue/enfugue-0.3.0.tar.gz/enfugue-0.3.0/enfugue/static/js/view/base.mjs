import{ElementBuilder}from"../base/builder.mjs";import{MutexLock}from"../base/mutex.mjs";import{isEmpty,deepClone}from"../base/helpers.mjs";const E=new ElementBuilder({tabs:"enfugue-tabs",tab:"enfugue-tab",tabContent:"enfugue-tab-content"});class View{static tagName="div";static className="view";static loaderClassName="loader";static classList=[];constructor(e){this.config=e,this.additionalClasses=deepClone(this.constructor.classList),this.hidden=!1,this.lock=new MutexLock}resize(){}hide(){return this.hidden=!0,this.lock.acquire().then((e=>{void 0!==this.node&&this.node.hide(),e()})),this}hideParent(){return this.hidden=!0,this.lock.acquire().then((e=>{void 0!==this.node&&void 0!==this.node.element&&(this.previousDisplay=this.node.element.parentElement.style.display,this.node.element.parentElement.classList.add("hidden")),e()})),this}show(){return this.hidden=!1,this.lock.acquire().then((e=>{void 0!==this.node&&this.node.show(),e()})),this}showParent(e="block"){return this.hidden=!1,this.lock.acquire().then((e=>{void 0!==this.node&&void 0!==this.node.element&&this.node.element.parentElement.classList.remove("hidden"),e()})),this}addClass(e){return this.additionalClasses.push(e),this.lock.acquire().then((t=>{void 0!==this.node&&this.node.addClass(e),t()})),this}removeClass(e){return this.additionalClasses=this.additionalClasses.filter((t=>t!==e)),this.lock.acquire().then((t=>{void 0!==this.node&&this.node.removeClass(e),t()})),this}hasClass(e){return-1!==this.additionalClasses.indexOf(e)||void 0!==this.node&&this.node.hasClass(e)}toggleClass(e){return this.hasClass(e)?this.removeClass(e):this.addClass(e)}async build(){return this.lock.acquire().then((e=>{let t=E.createElement(this.constructor.tagName);isEmpty(this.constructor.className)||t.addClass(this.constructor.className);for(let e of this.additionalClasses)t.addClass(e);return this.hidden&&t.hide(),e(),t}))}async getNode(){return void 0===this.node&&(this.node=await this.build()),this.node}async render(){return(await this.getNode()).render()}async loading(){return this.addClass(this.constructor.loaderClassName).addClass("loading").addClass("disabled"),this}async doneLoading(){return this.removeClass("loading").removeClass("disabled"),this}}class ShadowView extends View{static tagName=null;async build(){return this.lock.acquire().then((e=>{let t=E.createShadow();return e(),t}))}}class ParentView extends View{constructor(e){super(e),this.children=[]}getChild(e){return this.children[e]}isEmpty(){return 0===this.children.length}async empty(){return this.children=[],void 0!==this.node&&this.node.empty(),this}async insertChild(e,t){let s;if("function"==typeof t)s=new t(this.config,...Array.from(arguments).slice(2));else{if(!(t instanceof View))throw console.trace(),console.error(t),"Cannot add child of type "+typeof t;s=t}return s.parent=this,this.children=this.children.slice(0,e).concat([s]).concat(this.children.slice(e)),void 0!==this.node&&this.node.insert(e,await s.getNode()),s}async addChild(e){return this.insertChild(this.children.length,e,...Array.from(arguments).slice(1))}removeChild(e){for(let t of this.children)if(t==e)return this.children=this.children.filter((t=>t!=e)),void(void 0!==this.node&&this.node.remove(e.node));throw"Cannot find child to remove."}async build(){let e=await super.build();for(let t of this.children)e.append(await t.getNode());return e}}class TabbedView extends View{static tagName="enfugue-tabbed-view";constructor(e){super(e),this.tabs={},this.activeTab=null}async addTab(e,t){this.tabs[e]=t}async activateTab(e){if(this.activeTab=e,void 0!==this.node){let t=this.node.findAll(E.getCustomTag("tab"));for(let s of t)s.getText()==e?s.addClass("active"):s.removeClass("active");let s=this.tabs[e];s instanceof View&&(s=await s.getNode()),this.node.find(E.getCustomTag("tabContent")).content(s)}return this}async build(){let e=await super.build(),t=E.tabs(),s=E.tabContent();for(let e in this.tabs){let i=E.tab().content(e).on("click",(()=>this.activateTab(e)));if(t.append(i),null===this.activeTab&&(this.activeTab=e),this.activeTab===e){i.addClass("active");let t=this.tabs[e];t instanceof View&&(t=await t.getNode()),s.content(t)}}return e.content(t,s)}}export{View,ParentView,TabbedView,ShadowView};
