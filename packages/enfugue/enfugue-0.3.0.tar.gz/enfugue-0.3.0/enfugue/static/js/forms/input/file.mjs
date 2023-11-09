import{isEmpty}from"../../base/helpers.mjs";import{InputView}from"./base.mjs";class FileInputView extends InputView{static inputType="file";inputted(e){super.inputted(e),this.node.css({"background-size":"0% 100%"})}getValue(){if(void 0!==this.node&&this.node.element.files&&this.node.element.files.length>0)return this.node.element.files[0]}setProgress(e){this.progress=e,void 0!==this.node&&this.node.css({"background-size":100*this.progress+"% 100%"})}async build(){let e=await super.build(),s=isEmpty(this.progress)?0:this.progress;return e.css({"background-size":100*s+"% 100%"})}}export{FileInputView};
