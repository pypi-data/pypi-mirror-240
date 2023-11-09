import{isEmpty}from"../../base/helpers.mjs";import{ElementBuilder}from"../../base/builder.mjs";import{View}from"../../view/base.mjs";import{ImageAdjustmentFilter}from"../../graphics/image-adjust.mjs";import{ImagePixelizeFilter}from"../../graphics/image-pixelize.mjs";import{ImageSharpenFilter}from"../../graphics/image-sharpen.mjs";import{ImageBoxBlurFilter,ImageGaussianBlurFilter}from"../../graphics/image-blur.mjs";import{ImageFilterFormView,ImageAdjustmentFormView}from"../../forms/enfugue/image-editor.mjs";const E=new ElementBuilder;class ImageFilterView extends View{static filterFormView=ImageFilterFormView;constructor(e,t,i){super(e),this.image=t,this.container=i,this.cancelCallbacks=[],this.saveCallbacks=[],this.formView=new this.constructor.filterFormView(e),this.formView.onSubmit((e=>{this.setFilter(e)}))}createFilter(e,t=!0){switch(e){case"box":return new ImageBoxBlurFilter(this.image,t);case"gaussian":return new ImageGaussianBlurFilter(this.image,t);case"sharpen":return new ImageSharpenFilter(this.image,t);case"pixelize":return new ImagePixelizeFilter(this.image,t);case"adjust":return new ImageAdjustmentFilter(this.image,t);case"invert":return new ImageAdjustmentFilter(this.image,t,{invert:1});default:console.error("Bad filter",e)}}getImageSource(){return isEmpty(this.filter)?this.image:this.filter.imageSource}setFilter(e){null===e.filter?this.removeCanvas():void 0!==e.filter&&this.filterType!==e.filter&&(this.removeCanvas(),this.filter=this.createFilter(e.filter,!1),this.filterType=e.filter,this.filter.getCanvas().then((t=>{this.filter.setConstants(e),this.canvas=t,this.container.appendChild(this.canvas)}))),isEmpty(this.filter)||this.filter.setConstants(e)}removeCanvas(){if(!isEmpty(this.canvas)){try{this.container.removeChild(this.canvas)}catch(e){}this.canvas=null}}onCancel(e){this.cancelCallbacks.push(e)}onSave(e){this.saveCallbacks.push(e)}async saved(){for(let e of this.saveCallbacks)await e()}async canceled(){for(let e of this.cancelCallbacks)await e()}async build(){let e=await super.build(),t=E.button().class("column").content("Reset"),i=E.button().class("column").content("Save"),s=E.button().class("column").content("Cancel"),a=E.div().class("flex-columns half-spaced margin-top padded-horizontal").content(t,i,s);return t.on("click",(()=>{this.formView.setValues(this.constructor.filterFormView.defaultValues),setTimeout((()=>{this.formView.submit()}),100)})),i.on("click",(()=>this.saved())),s.on("click",(()=>this.canceled())),e.content(await this.formView.getNode(),a),e}}class ImageAdjustmentView extends ImageFilterView{static filterFormView=ImageAdjustmentFormView;constructor(e,t,i){super(e,t,i),this.setFilter({filter:"adjust"})}}export{ImageFilterView,ImageAdjustmentView};
