import{ElementBuilder}from"../base/builder.mjs";import{SimpleNotification}from"../common/notify.mjs";import{View}from"./base.mjs";import{StringInputView,ListInputView}from"../forms/input.mjs";import{set,isEmpty,snakeCase,deepClone,stripHTML}from"../base/helpers.mjs";const E=new ElementBuilder({tablePaging:"enfugue-model-table-paging",tableSearching:"enfugue-model-table-searching"});class TableView extends View{static tagName="table";static buttons=[];static emptyRow="No Data";static applyDefaultSort=!0;static canSort=!0;static columnFormatters={};static columns=[];static sort=[];constructor(t,s){super(t),this.data=[],this.buttons=[],this.onSortCallbacks=[],this.applyDefaultSort=this.constructor.applyDefaultSort,this.sort=deepClone(this.constructor.sort),this.columnFormatters=deepClone(this.constructor.columnFormatters),this.columns=deepClone(this.constructor.columns),isEmpty(s)||this.setData(s,isEmpty(this.columns))}addButton(t,s,e){this.buttons.push({label:t,icon:s,click:e})}setFormatter(t,s){this.columnFormatters[t]=s}onSort(t){this.onSortCallbacks.push(t)}onSearch(t){this.onSearchCallbacks.push(t)}async setData(t,s,e=!0){if(this.data=t,!1!==s)try{this.columns=Object.getOwnPropertyNames(this.data[0]),this.sort=this.sort.filter((([t,s])=>-1!==this.columns.indexOf(t)))}catch{this.columns=[],this.sort=[]}if(e&&await this.sortData(!1),void 0!==this.node){let t=this.node.find("thead"),e=this.node.find("tbody");if(!1!==s&&t.content(await this.buildHeaderRow()),0===this.data.length)e.content(await this.buildEmptyRow());else{e.empty();for(let t of this.data)e.append(await this.buildDataRow(t));e.render()}}}addDatum(t,s){if(this.data.push(t),!0===s&&(this.columns=Object.getOwnPropertyNames(t),this.sort=this.sort.filter((([t,s])=>-1!==this.columns.indexOf(t)))),void 0!==this.node){let e=this.node.find("thead"),i=this.node.find("tbody");!0===s&&e.content(this.buildHeaderRow()),i.append(this.buildDataRow(t))}}setColumns(t){this.columns=t,this.sort=this.sort.filter((([t,s])=>Array.isArray(this.columns)?-1!==this.columns.indexOf(t):void 0!==this.columns[t])),void 0!==this.node&&this.node.find("thead").content(this.buildHeaderRow())}setEmpty(t){void 0!==t&&this.setColumns(t),this.data=[],void 0!==this.node&&this.node.find("tbody").content(this.buildEmptyRow())}async sortData(t=!0){this.data.sort(((t,s)=>{for(let[e,i]of this.sort){let a,o=t[e],n=s[e];if("string"==typeof o&&"string"==typeof n&&(a=o.localeCompare(n)),void 0===a)try{a=o<n?-1:o==n?0:1}catch(e){return console.error("Error caught during sorting, likely due to incomparable types."),console.error(e),console.log("Left operand",t,"left value",o),console.log("Right operand",s,"right value",n),0}if(0!==a)return a*(i?-1:1)}return 0})),t&&await this.setData(this.data,!1,!1)}async sortChanged(){for(let t of this.onSortCallbacks)await t(this.sort);this.applyDefaultSort&&this.sortData()}async buildHeaderRow(){let t=E.tr(),s={},e=Array.isArray(this.columns)?this.columns:Object.getOwnPropertyNames(this.columns),i=Array.isArray(this.columns)?this.columns:e.map((t=>this.columns[t]));for(let a in e){let o=e[a],n=i[a],r=n+"<br/><em class='note'>Left-click to toggle sort.</em>",l=E.th().content(n).class(snakeCase(o)).data("tooltip",r),h=-1;for(let t=0;t<this.sort.length;t++){let[s,e]=this.sort[t];if(s===o){h=t;break}}if(s[o]=l,-1!==h){l.addClass("sort"),this.sort[h][1]&&l.addClass("sort-reverse"),l.addClass(`sort-${h}`)}this.constructor.canSort&&l.on("click",(t=>{if(l.hasClass("sort"))if(l.hasClass("sort-reverse")){l.removeClass("sort").removeClass("sort-reverse"),this.sort=this.sort.filter((([t,s])=>t!==o));let t=0;for(let[e,i]of this.sort){for(let t=0;t<9;t++)s[e].removeClass(`sort-${t}`);s[e].addClass("sort-"+t++)}this.sortChanged()}else{l.addClass("sort-reverse");for(let t=0;t<this.sort.length;t++)if(this.sort[t][0]===o){this.sort[t][1]=!0;break}this.sortChanged()}else this.sort.length<9&&(l.addClass("sort").addClass(`sort-${this.sort.length}`),this.sort.push([o,!1]),this.sortChanged())})),t.append(l)}for(let s of this.constructor.buttons.concat(this.buttons))t.append(E.th().content(s.label).class(snakeCase(s.label)).addClass("button-column"));return t}async buildEmptyRow(){return E.tr().content(E.td().content(this.constructor.emptyRow).attr("colspan",this.columns.length+this.constructor.buttons.length+this.buttons.length))}async defaultFormatter(t){return"string"!=typeof t?null===t?"None":void 0===t?"":"boolean"==typeof t?t?"True":"False":void 0!==t.toLocaleString?t.toLocaleString():JSON.stringify(t):t}async buildDataRow(t){let s=E.tr(),e=Array.isArray(this.columns)?this.columns:Object.getOwnPropertyNames(this.columns);for(let i of e){let e=t[i];e=null==this.columnFormatters[i]?await this.defaultFormatter(e):await this.columnFormatters[i].call(this,e,t);let a=e,o=E.td().content(e).class(snakeCase(i));isEmpty(a)||"string"!=typeof a||o.data("tooltip",a),s.append(o)}for(let e of this.constructor.buttons.concat(this.buttons)){let i=E.button().class("round").content(E.i().class(e.icon));i.data("tooltip",e.label),i.on("click",(()=>e.click.call(this,t))),s.append(E.td().content(i).class(snakeCase(e.label)).addClass("button-column"))}return s}async build(){let t=await super.build(),s=await this.buildHeaderRow(),e=E.thead().content(s),i=E.tbody();if(0===this.data.length)i.append(await this.buildEmptyRow());else for(let t of this.data)i.append(await this.buildDataRow(t));return t.append(e,i)}}class ModelTableView extends View{static tagName="enfugue-model-table";static limit=10;static pageWindowSize=2;static searchTimeout=250;static columnFormatters={};static columns=[];static sortGroups=[];static buttons=[];static searchFields=[];constructor(t,s,e){if(super(t),this.modelObject=s,this.filter=isEmpty(e)?{}:e,this.limit=this.constructor.limit,this.pageIndex=0,this.customColumns=!1,this.pages={},this.table=new TableView(t),this.table.parent=this,this.table.applyDefaultSort=!1,this.sortGroups=deepClone(this.constructor.sortGroups),this.searchFields=deepClone(this.constructor.searchFields),this.table.sort=this.sortGroups.map((t=>[t.column,"desc"===t.direction])),this.table.onSort((t=>{this.tableSort=t})),!isEmpty(this.constructor.columnFormatters))for(let t in this.constructor.columnFormatters){let s=this.constructor.columnFormatters[t];this.table.setFormatter(t,s)}if(isEmpty(this.constructor.columns)||(this.customColumns=!0,this.table.setColumns(this.constructor.columns)),!isEmpty(this.constructor.buttons))for(let t of this.constructor.buttons)this.table.addButton(t.label,t.icon,t.click);this.paging=new ListInputView(t),this.paging.setOptions(["1"]),this.paging.setValue("1",!1),this.paging.onChange((()=>this.setPageIndex(parseInt(this.paging.getValue())-1)))}executeQuery(t){let s={limit:this.limit,offset:this.pageIndex*this.limit};return isEmpty(this.sortGroups)||(s.sort=this.sortGroups.map((t=>`${t.column}:${t.direction}`))),isEmpty(this.searchFields)||isEmpty(this.searchValue)||(s.ilike=this.searchFields.map((t=>`${t}:${encodeURIComponent(this.searchValue)}`))),this.modelObject.query(this.filter,s,t)}get page(){return this.pages[this.pageIndex]}set page(t){this.pages[this.pageIndex]=t}get pageSize(){return this.limit}get tableSort(){return isEmpty(this.sortGroups)?[]:this.sortGroups}set tableSort(t){this.sortGroups=t.map((([t,s])=>({column:t,direction:s?"desc":"asc"}))),this.requery()}set tableSearch(t){this.searchValue=t,this.requery()}get pageWindow(){let t=Math.max(1,this.pageIndex+1-this.constructor.pageWindowSize),s=Math.min(t+2*this.constructor.pageWindowSize,1===this.count?1:this.pageCount+1),e=s-t,i=2*this.constructor.pageWindowSize+1;if(e<i&&this.pageCount>i){let s=i-e;t=Math.max(1,t-s+1)}return new Array(s-t+1).fill(null).map(((s,e)=>`${e+t}`))}get pageOptions(){let t=this.pageWindow,s=this.pageIndex>this.constructor.pageWindowSize,e=this.pageIndex<this.pageCount-this.constructor.pageWindowSize;return s&&(t=["1"].concat(t)),e&&t.push(`${this.pageCount+1}`),t}get rowRangeString(){if(0==this.count)return"";return`${this.pageSize*this.pageIndex+1} — ${Math.min(this.count,(this.pageIndex+1)*this.pageSize)} of ${this.count}`}async setPageIndex(t){this.pageIndex!==t&&(this.paging.disable(),this.pageIndex=t,this.paging.setOptions(this.pageOptions),this.paging.setValue(this.pageIndex+1,!1),await this.table.setData(await this.getTableData(),!this.customColumns),void 0!==this.node&&this.node.find(E.getCustomTag("tablePaging")).find("span").content(this.rowRangeString),this.pageIndex>this.constructor.pageWindowSize+1?this.paging.addClass("include-first"):this.paging.removeClass("include-first"),this.pageIndex<this.pageCount-this.constructor.pageWindowSize-1?this.paging.addClass("include-last"):this.paging.removeClass("include-last"),this.paging.enable())}async getTableData(){if(isEmpty(this.page)){let t,s;isEmpty(this.count)?([t,s]=await this.executeQuery(!0),this.count=s.count,this.pageCount=this.count>1?Math.floor((this.count-1)/this.pageSize):this.count,this.paging.setOptions(this.pageOptions),this.paging.setValue("1",!1),this.pageIndex>this.constructor.pageWindowSize+1?this.paging.addClass("include-first"):this.paging.removeClass("include-first"),this.pageIndex<this.pageCount-this.constructor.pageWindowSize-1?this.paging.addClass("include-last"):this.paging.removeClass("include-last")):t=await this.executeQuery(),isEmpty(t)?this.page=[]:Array.isArray(t)?this.page=t:this.page=[t]}return this.page}async requery(){this.pages={},this.count=null,await this.getTableData();let t=this.pageIndex;this.pageIndex=null,await this.setPageIndex(t)}addButton(t,s,e){this.table.addButton(t,s,e)}setColumns(t){this.customColumns=t,this.table.setColumns(t)}setFormatter(t,s){this.table.setFormatter(t,s)}setSearchFields(t){this.searchFields=t}debounceSearch(t){clearTimeout(this.searchTimer),this.searchTimer=setTimeout((()=>{this.tableSearch=t}),this.constructor.searchTimeout)}async build(){let t=await super.build(),s=E.tableSearching(),e=E.tablePaging(),i=new StringInputView(this.config,"search",{placeholder:"Start typing to search…"});return i.onInput((t=>this.debounceSearch(t))),s.content(await i.getNode()),isEmpty(this.modelObject)||this.table.setData(await this.getTableData(),isEmpty(this.customColumns)),e.content(await this.paging.getNode(),E.span().content(this.rowRangeString)),t.content(s,await this.table.getNode(),e),t}}export{TableView,ModelTableView};
