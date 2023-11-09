import{isEmpty}from"./helpers.mjs";class API{static allMethods=["get","put","post","delete","patch","head","options","trace","connect"];static requestTimeout=9e4;constructor(t,e){this.timeout=this.constructor.requestTimeout,this.baseUrl=t?encodeURI(t.endsWith("/")?t.substring(0,t.length-1):t):"",this.debug=!0===e;for(let t of this.constructor.allMethods)this[t]=(e,s,n,o,r)=>this.query(t,e,s,n,o,r)}buildUrl(t,e){let s;if(void 0===t&&(t=""),void 0===t)s=this.baseUrl;else if(Array.isArray(t))s=[this.baseUrl].concat(t.map((t=>encodeURIComponent(t)))).join("/");else if(t.startsWith("http"))s=t;else if(t.startsWith("//")){s=`${"https"===window.location.href.substring(0,5)?"https":"http"}://${t}`}else t.startsWith("/")&&(t=t.substring(1)),s=`${this.baseUrl}/${encodeURI(t)}`;if(void 0!==e&&Object.getOwnPropertyNames(e).length>0){s=`${s}?${Object.getOwnPropertyNames(e).map((t=>Array.isArray(e[t])?e[t].map((e=>`${t}=${encodeURIComponent(e)}`)).join("&"):`${t}=${encodeURIComponent(e[t])}`)).join("&")}`}return s}query(t,e,s,n,o,r){s=s||{},n=n||{},o=o||{},r=r||(()=>{}),t=t.toUpperCase();let i=this.debug,a=this.timeout;return new Promise(((l,h)=>{let u=new XMLHttpRequest,d=this.buildUrl(e,n);u.addEventListener("load",(function(){i&&console.log("Response from",d,":",this.responseText),4===this.readyState&&this.status>=200&&this.status<400?l(this.responseText):h(this)})),u.addEventListener("error",(function(t){h(this)})),u.addEventListener("timeout",(function(t){h(this)})),u.upload.onprogress=r,u.timeout=a,i&&console.log(t,"Request to",d,o);try{u.open(t,d);for(let t in s)u.setRequestHeader(t,s[t]);u.send(isEmpty(o)?void 0:o)}catch(t){h(u,t)}}))}download(t,e,s,n,o){return s=s||{},n=n||{},o=o||{},new Promise(((r,i)=>{let a=new XMLHttpRequest,l=this.buildUrl(e,n);a.responseType="blob",a.addEventListener("load",(function(){if(4===this.readyState&&this.status>=200&&this.status<400){let t=this.response,e=this.getResponseHeader("Content-Disposition").match(/filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/)[1],s=document.createElement("a");(e.startsWith('"')||e.startsWith("'"))&&(e=e.substring(1)),(e.endsWith('"')||e.endsWith("'"))&&(e=e.substring(0,e.length-1)),s.href=window.URL.createObjectURL(t),s.download=e,s.dispatchEvent(new MouseEvent("click")),r()}else i(this)}));try{a.open(t,l);for(let t in s)a.setRequestHeader(t,s[t]);a.send(o)}catch(t){i(a,t)}}))}}class JSONAPI extends API{async download(t,e,s,n,o){return s=s||{},-1!=["POST","PUT","PATCH"].indexOf(t.toUpperCase())&&(s["Content-Type"]="application/json",o=null==o?null:JSON.stringify(o)),super.download(t,e,s,n,o)}rawQuery(t,e,s,n,o,r){return super.query(t,e,s,n,o,r)}async query(t,e,s,n,o,r){s=s||{},-1==["POST","PUT","PATCH"].indexOf(t.toUpperCase())||isEmpty(o)||(s["Content-Type"]="application/json");let i,a,l=!1;try{i=await super.query(t,e,s,n,isEmpty(o)?null:JSON.stringify(o),r)}catch(t){l=!0,i=t.responseText}try{a=JSON.parse(i)}catch(t){a=i,this.debug&&(console.warn("Couldn't parse \""+i+'"'),console.error(t))}if(l)throw a;return a}}export{API,JSONAPI};
