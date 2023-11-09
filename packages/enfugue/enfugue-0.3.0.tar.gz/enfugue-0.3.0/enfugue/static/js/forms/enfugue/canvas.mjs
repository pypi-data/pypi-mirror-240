import{isEmpty}from"../../base/helpers.mjs";import{FormView}from"../base.mjs";import{NumberInputView,CheckboxInputView,SelectInputView,MaskTypeInputView,EngineSizeInputView}from"../input.mjs";let defaultWidth=512,defaultHeight=512,defaultTilingStride=64;if(!(isEmpty(window.enfugue)||isEmpty(window.enfugue.config)||isEmpty(window.enfugue.config.model)||isEmpty(window.enfugue.config.model.invocation))){let e=window.enfugue.config.model.invocation;isEmpty(e.width)||(defaultWidth=e.width),isEmpty(e.height)||(defaultHeight=e.height),isEmpty(e.tilingSize)||(defaultTilingStride=e.tilingSize)}class CanvasFormView extends FormView{static className="canvas-form-view";static autoSubmit=!0;static fieldSets={Dimensions:{width:{label:"Width",class:NumberInputView,config:{min:64,max:16384,value:defaultWidth,step:8,tooltip:"The width of the canvas in pixels.",allowNull:!1}},height:{label:"Height",class:NumberInputView,config:{min:64,max:16384,value:defaultHeight,step:8,tooltip:"The height of the canvas in pixels.",allowNull:!1}},tileHorizontal:{label:"Horizontally<br/>Tiling",class:CheckboxInputView,config:{tooltip:"When enabled, the resulting image will tile horizontally, i.e., when duplicated and placed side-by-side, there will be no seams between the copies."}},tileVertical:{label:"Vertically<br/>Tiling",class:CheckboxInputView,config:{tooltip:"When enabled, the resulting image will tile vertically, i.e., when duplicated and placed with on image on top of the other, there will be no seams between the copies."}},useTiling:{label:"Enabled Tiled Diffusion/VAE",class:CheckboxInputView,config:{tooltip:"When enabled, the engine will only ever process a square in the size of the configured model size at once. After each square, the frame will be moved by the configured amount of pixels along either the horizontal or vertical axis, and then the image is re-diffused. When this is disabled, the entire canvas will be diffused at once. This can have varying results, but a guaranteed result is increased VRAM use.",value:!1}},tilingSize:{label:"Tile Size",class:EngineSizeInputView,config:{required:!1,value:null}},tilingStride:{label:"Tile Stride",class:SelectInputView,config:{options:["8","16","32","64","128","256","512"],value:`${defaultTilingStride}`,tooltip:"The number of pixels to move the frame when doing tiled diffusion. A low number can produce more detailed results, but can be noisy, and takes longer to process. A high number is faster to process, but can have poor results especially along frame boundaries. The recommended value is set by default."}},tilingMaskType:{label:"Tile Mask",class:MaskTypeInputView}}};async submit(){await super.submit();let e=await this.getInputView("useTiling");this.values.tileHorizontal||this.values.tileVertical?(this.removeClass("no-tiling"),e.setValue(!0,!1),e.disable()):(e.enable(),this.values.useTiling?this.removeClass("no-tiling"):this.addClass("no-tiling"))}}export{CanvasFormView};
