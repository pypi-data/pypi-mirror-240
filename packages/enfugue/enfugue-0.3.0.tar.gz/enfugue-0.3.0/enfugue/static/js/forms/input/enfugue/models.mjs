import{isEmpty,deepClone,createElementsFromString}from"../../../base/helpers.mjs";import{FormView}from"../../base.mjs";import{InputView}from"../base.mjs";import{StringInputView,TextInputView}from"../string.mjs";import{NumberInputView,FloatInputView}from"../numeric.mjs";import{FormInputView,RepeatableInputView}from"../parent.mjs";import{SelectInputView,SearchListInputView,SearchListInputListView}from"../enumerable.mjs";class ModelPickerListInputView extends SearchListInputListView{static classList=SearchListInputListView.classList.concat(["model-picker-list-input-view"])}class ModelPickerStringInputView extends StringInputView{setValue(t,e){return isEmpty(t)||(t.startsWith("<")?t=createElementsFromString(t)[0].innerText:-1!==t.indexOf("/")&&(t=t.split("/")[1])),super.setValue(t,e)}}class ModelPickerInputView extends SearchListInputView{static placeholder="Start typing to search models…";static stringInputClass=ModelPickerStringInputView;static listInputClass=ModelPickerListInputView}class DefaultVaeInputView extends SelectInputView{static defaultOptions={ema:"EMA 560000",mse:"MSE 840000",xl:"SDXL",xl16:"SDXL FP16",other:"Other"};static placeholder="Default";static allowEmpty=!0;static tooltip="Variational Autoencoders are the model that translates images between pixel space - images that you can see - and latent space - images that the AI model understands. In general you do not need to select a particular VAE model, but you may find slight differences in sharpness of resulting images."}class VaeInputView extends InputView{static tagName="enfugue-vae-input-view";static selectClass=DefaultVaeInputView;static textClass=StringInputView;static textInputConfig={placeholder:"e.g. stabilityai/sdxl-vae",tooltip:"Enter the name of a HuggingFace repository housing the VAE configuration. Visit https://huggingface.co for more information."};constructor(t,e,i){super(t,e,i),this.defaultInput=new this.constructor.selectClass(t,"default"),this.otherInput=new this.constructor.textClass(t,"other",this.constructor.textInputConfig),this.defaultInput.onChange((()=>{let t=this.defaultInput.getValue();"other"===t?(this.value="",this.otherInput.show()):(this.value=t,this.otherInput.hide()),this.changed()})),this.otherInput.onChange((()=>{"other"===this.defaultInput.getValue()&&(this.value,this.otherInput.getValue(),this.changed())})),this.otherInput.hide()}getValue(){let t=this.defaultInput.getValue();return"other"===t?this.otherInput.getValue():t}setValue(t,e){super.setValue(t,!1),isEmpty(t)?(this.defaultInput.setValue(null,!1),this.otherInput.setValue("",!1),this.otherInput.hide()):-1===Object.getOwnPropertyNames(DefaultVaeInputView.defaultOptions).indexOf(t)?(this.defaultInput.setValue("other",!1),this.otherInput.setValue(t,!1),this.otherInput.show()):(this.defaultInput.setValue(t,!1),this.otherInput.setValue("",!1),this.otherInput.hide()),e&&this.changed()}async build(){return(await super.build()).content(await this.defaultInput.getNode(),await this.otherInput.getNode())}}class InversionInputView extends SearchListInputView{static stringInputClass=ModelPickerStringInputView}class LoraInputView extends SearchListInputView{static stringInputClass=ModelPickerStringInputView}class LycorisInputView extends SearchListInputView{static stringInputClass=ModelPickerStringInputView}class CheckpointInputView extends SearchListInputView{static stringInputClass=ModelPickerStringInputView}class MotionModuleInputView extends SearchListInputView{static stringInputClass=ModelPickerStringInputView}class LoraFormView extends FormView{static autoSubmit=!0;static fieldSets={LoRA:{model:{label:"Model",class:LoraInputView,config:{required:!0}},weight:{label:"Weight",class:FloatInputView,config:{min:0,value:1,step:.01,required:!0}}}}}class LoraFormInputView extends FormInputView{static formClass=LoraFormView}class LycorisFormView extends FormView{static autoSubmit=!0;static fieldSets={LyCORIS:{model:{label:"Model",class:LycorisInputView,config:{required:!0}},weight:{label:"Weight",class:FloatInputView,config:{min:0,value:1,step:.01,required:!0}}}}}class LycorisFormInputView extends FormInputView{static formClass=LycorisFormView}class MultiLoraInputView extends RepeatableInputView{static noItemsLabel="No LoRA Configured";static addItemLabel="Add LoRA";static memberClass=LoraFormInputView}class MultiLycorisInputView extends RepeatableInputView{static noItemsLabel="No LyCORIS Configured";static addItemLabel="Add LyCORIS";static memberClass=LycorisFormInputView}class MultiInversionInputView extends RepeatableInputView{static noItemsLabel="No Textual Inversion Configured";static addItemLabel="Add Textual Inversion";static memberClass=InversionInputView}class ModelMergeModeInputView extends SelectInputView{static defaultOptions={"add-difference":"Add Difference","weighted-sum":"Weighted Sum"}}export{CheckpointInputView,LoraInputView,LycorisInputView,InversionInputView,MultiLoraInputView,MultiLycorisInputView,MultiInversionInputView,VaeInputView,DefaultVaeInputView,ModelPickerStringInputView,ModelPickerListInputView,ModelPickerInputView,ModelMergeModeInputView,MotionModuleInputView};
