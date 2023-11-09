import{InputView}from"./base.mjs";import{FormView}from"../base.mjs";import{ElementBuilder}from"../../base/builder.mjs";import{isEmpty}from"../../base/helpers.mjs";const E=new ElementBuilder({repeatableItem:"enfugue-repeatable-input-item"});class RepeatableInputView extends InputView{static tagName="enfugue-repeatable-input";static addItemLabel="+";static removeItemLabel="×";static noItemsLabel="Press `+` to add an item";static memberClass=InputView;static memberConfig={};static minimumItems=0;static maximumItems=1/0;constructor(e,t,i){super(e,t,i),this.inputViews=[];let s=i.members||{};this.memberConfig={...this.constructor.memberConfig,...s};for(let e=0;e<this.constructor.minimumItems;e++)this.addInput()}getValue(){return this.inputViews.map((e=>e.getValue()))}setValue(e,t){let i=isEmpty(e)?[]:Array.isArray(e)?e:[e],s=this.inputViews.length,n=i.length;for(let e=0;e<n;e++)e>=s?this.addInput({value:i[e]}):this.inputViews[e].setValue(i[e]);if(n<s&&(this.inputViews=this.inputViews.slice(0,n)),void 0!==this.node){let e=s-n;for(let t=0;t<e;t++){let e=this.node.getChild(-2);"add-item"!==e.className&&this.node.remove(e)}this.inputViews.length<=this.constructor.minimumItems?this.disableRemove():this.enableRemove(),0===this.inputViews.length?this.addClass("no-children"):this.removeClass("no-children")}super.setValue(e,t)}disable(){super.disable();for(let e of this.inputViews)e.disable();void 0!==this.node&&(this.node.find("input.add-item").disabled(!0).addClass("disabled"),this.disableRemove())}disableRemove(){if(void 0!==this.node)for(let e of this.node.findAll("input.remove-item"))e.disabled(!0).addClass("disabled")}enable(){super.enable();for(let e of this.inputViews)e.enable();void 0!==this.node&&(this.node.find("input.add-item").disabled(!1).removeClass("disabled"),this.enableRemove())}enableRemove(){if(void 0!==this.node)for(let e of this.node.findAll("input.remove-item"))e.disabled(!1).removeClass("disabled")}addInput(e){e=e||{};let t={...this.memberConfig,...e},i=new this.constructor.memberClass(this.config,this.inputViews.length,t);return i.inputParent=this,void 0!==t.value&&i.setValue(t.value,!1),i.onChange((()=>this.changed())),this.inputViews.push(i),void 0!==this.node&&i.getNode().then((e=>{let t=this.node.find("input.add-item"),s=E.repeatableItem().content(e),n=E.input().type("button").class("remove-item").value(this.constructor.removeItemLabel);n.on("click",(async e=>{this.node.remove(s),this.inputViews=this.inputViews.filter((e=>i.fieldName!==e.fieldName));for(let e=0;e<this.inputViews.length;e++)this.inputViews[e].fieldName=e;this.inputViews.length<=this.constructor.minimumItems&&this.disableRemove(),0==this.inputViews.length&&this.addClass("no-children"),t.removeClass("disabled"),this.changed()})),this.inputViews.length>=this.constructor.maximumItems&&t.addClass("disabled"),this.inputViews.length<=this.constructor.minimumItems?n.disabled(!0).addClass("disabled"):this.enableRemove(),this.node.insertBefore(t,s.append(n)),this.removeClass("no-children")})),i}async build(){let e=await super.build(),t=E.div().class("empty-placeholder").content(this.constructor.noItemsLabel),i=E.input().type("button").class("add-item").value(this.constructor.addItemLabel);e.append(t),isEmpty(this.inputViews)&&e.addClass("no-children");for(let t of this.inputViews){let s=E.repeatableItem().content(await t.getNode()),n=E.input().type("button").class("remove-item").value(this.constructor.removeItemLabel);n.on("click",(async n=>{e.remove(s),this.inputViews=this.inputViews.filter((e=>t.fieldName!==e.fieldName));for(let e=0;e<this.inputViews.length;e++)this.inputViews[e].fieldName=e;this.inputViews.length<=this.constructor.minimumItems&&this.disableRemove(),0==this.inputViews.length&&this.addClass("no-children"),i.removeClass("disabled"),this.changed()})),this.inputViews.length<=this.constructor.minimumItems&&n.disabled(!0).addClass("disabled"),e.append(s.append(n))}return i.on("click",(()=>i.hasClass("disabled")?0:this.addInput()&&this.changed())),e.append(i),e}}class FormInputView extends InputView{static tagName="enfugue-form-input-view";static formClass=FormView;constructor(e,t,i){super(e,t,i),this.form=new this.constructor.formClass(e),isEmpty(this.value)||this.form.setValues(this.value),this.form.onSubmit((()=>this.changed()))}getValue(){return this.form.values}setValue(e){this.form.setValues(e)}async build(){return await this.form.getNode()}}export{RepeatableInputView,FormInputView};
