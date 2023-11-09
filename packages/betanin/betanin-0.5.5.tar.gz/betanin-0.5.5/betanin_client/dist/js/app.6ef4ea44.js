(function(t){function e(e){for(var r,o,a=e[0],c=e[1],u=e[2],d=0,f=[];d<a.length;d++)o=a[d],Object.prototype.hasOwnProperty.call(s,o)&&s[o]&&f.push(s[o][0]),s[o]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(t[r]=c[r]);l&&l(e);while(f.length)f.shift()();return i.push.apply(i,u||[]),n()}function n(){for(var t,e=0;e<i.length;e++){for(var n=i[e],r=!0,a=1;a<n.length;a++){var c=n[a];0!==s[c]&&(r=!1)}r&&(i.splice(e--,1),t=o(o.s=n[0]))}return t}var r={},s={app:0},i=[];function o(e){if(r[e])return r[e].exports;var n=r[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.m=t,o.c=r,o.d=function(t,e,n){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)o.d(n,r,function(e){return t[e]}.bind(null,r));return n},o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="/";var a=window["webpackJsonp"]=window["webpackJsonp"]||[],c=a.push.bind(a);a.push=e,a=a.slice();for(var u=0;u<a.length;u++)e(a[u]);var l=c;i.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"0370":function(t,e,n){"use strict";n("7cb8")},1282:function(t,e,n){},"1eb3":function(t,e,n){"use strict";n("4324")},"341a":function(t,e,n){},3555:function(t,e,n){"use strict";n("7beb")},"37c3":function(t,e,n){},"3b51":function(t,e,n){},"3f21":function(t,e,n){"use strict";n("3b51")},4324:function(t,e,n){},"481a":function(t,e,n){"use strict";n("ae42")},"49b9":function(t,e,n){"use strict";n("6653")},"56d7":function(t,e,n){"use strict";n.r(e);var r=n("5530"),s=(n("e260"),n("e6cf"),n("cca6"),n("a79d"),n("2b0e")),i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("router-view")},o=[],a=n("2877"),c={},u=Object(a["a"])(c,i,o,!1,null,null,null),l=u.exports,d=n("8c4f"),f={clearToken:function(){delete localStorage.token},setToken:function(t){localStorage.token=t},getToken:function(){return localStorage.token},isLoggedIn:function(){return void 0!==localStorage.token}},p=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"container"},[n("div",{attrs:{id:"app"}},[n("div",{staticClass:"main-section"},[n("nav-bar")],1),n("div",{staticClass:"main-section"},[n("router-view")],1)]),n("div",{attrs:{id:"footer"}},[n("div",{staticClass:"main-section"},[n("connection-banner")],1)])])},v=[],m=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"banner"},[n("div",{directives:[{name:"show",rawName:"v-show",value:!t.getConnected,expression:"!getConnected"}],staticClass:"disconnected"},[n("p",[t._v("disconnected")])]),n("div",{staticClass:"version"},[n("p",[t._v(t._s(t.getSystemInfo.betaninVersion))])]),n("div",{staticClass:"status"},[n("p",[n("b",[t._v(t._s(t.getTotal))]),t._v(" imports, "+t._s(t.getActiveCount)+" active")])])])},b=[],g=n("2f62"),h=n("ade3"),_=n("b85c"),y=n("1da1"),w=(n("96cf"),n("4de4"),n("d3b7"),n("07ac"),n("ac1f"),n("5319"),{login:function(t,e){return Object(y["a"])(regeneratorRuntime.mark((function n(){var r;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return n.prev=0,n.next=3,$.insecureAxios.post("authentication/login",{username:t,password:e});case 3:r=n.sent,f.setToken(r.data.token),bn.replace(bn.currentRoute.query.redirect||"/"),n.next=15;break;case 8:if(n.prev=8,n.t0=n["catch"](0),void 0===n.t0.response||422!==n.t0.response.status){n.next=14;break}return n.abrupt("return",n.t0.response.data.message);case 14:return n.abrupt("return","unexpected error while fetching a token from the backend");case 15:case"end":return n.stop()}}),n,null,[[0,8]])})))()},logout:function(t){f.clearToken(),bn.replace({name:"login",query:{redirect:t}})}}),x=n("bc3a"),C=n.n(x),O=!0,k="http://",S="localhost",T=9393,E="/api",j=O?"/":k+S+":"+T,I=O?E:k+S+":"+T+E,P={baseURL:I,timeout:5e3,headers:{"Content-Type":"application/json"}},A=C.a.create(P),D=C.a.create(P);D.interceptors.request.use((function(t){return t.headers["Authorization"]="Bearer ".concat(f.getToken()),t}),void 0),D.interceptors.response.use(void 0,(function(t){return void 0===t.response||401!==t.response.status&&422!==t.response.status||"/login"===bn.currentRoute.path||w.logout(bn.currentRoute.fullPath),Promise.reject(t)}));var R,N,L,$={insecureAxios:A,secureAxios:D},F="TORRENTS_ONE_UPDATE",U="TORRENTS_ONE_DELETE",B="TORRENTS_ALL_APPEND",M="LINES_CREATE",q="NOTI_STRINGS_UPDATE",V="NOTI_STRING_UPDATE",K="NOTI_POSSIBLE_UPDATE",z="NOTI_SERVICES_UPDATE",G="NOTI_SERVICE_CREATE",X="NOTI_SERVICE_DELETE",H="NOTI_SERVICE_UPDATE",J="NOTI_SERVICE_TESTING_UPDATE",Y="STATUS_CONNECTED_UPDATE",Q="STATUS_SYSTEM_UPDATE",W={torrents:{},total:0},Z={getTorrent:function(t){return function(e){return t.torrents[e]}},getTotal:function(t){return t.total},getActive:function(t){return Object.values(t.torrents).filter((function(t){return"COMPLETED"!==t.status}))},getActiveCount:function(t,e){return e.getActive.length}},tt={doFetchOne:function(t,e){return Object(y["a"])(regeneratorRuntime.mark((function n(){var r,s;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return r=t.commit,n.next=3,$.secureAxios.get("torrents/".concat(e));case 3:s=n.sent,r(F,s.data);case 5:case"end":return n.stop()}}),n)})))()},doDeleteOne:function(t,e){var n=t.commit;$.secureAxios.delete("torrents/".concat(e)),n(U,e)},doRetryOne:function(t,e){$.secureAxios.put("torrents/".concat(e))},doSocket__newTorrent:function(t,e){var n=t.commit;n(F,e)}},et=(R={},Object(h["a"])(R,B,(function(t,e){var n=e.total,r=e.torrents;s["a"].set(t,"total",n);var i,o=Object(_["a"])(r);try{for(o.s();!(i=o.n()).done;){var a=i.value;s["a"].set(t.torrents,a.id,a)}}catch(c){o.e(c)}finally{o.f()}})),Object(h["a"])(R,F,(function(t,e){s["a"].set(t.torrents,e.id,e)})),Object(h["a"])(R,U,(function(t,e){s["a"].delete(t.torrents,e)})),R),nt={state:W,getters:Z,actions:tt,mutations:et,namespaced:!0},rt=(n("159b"),n("3835")),st=(n("a434"),n("4fad"),function t(e,n,r,s){var i,o;null!==(i=r)&&void 0!==i||(r=0),null!==(o=s)&&void 0!==o||(s=e.length-1);var a=r+Math.floor((s-r)/2);0===e.length?e.push(n):n.index>e[s].index?e.splice(s+1,0,n):n.index<e[r].index?e.splice(r,0,n):n.index<e[a].index?t(e,n,r,a-1):n.index>e[a].index&&t(e,n,a+1,s)}),it=function(t){for(var e={torrent_id:"torrentID"},n=0,r=Object.entries(t);n<r.length;n++){var s=Object(rt["a"])(r[n],2),i=s[0],o=s[1];if(i in e)delete t[i],t[e[i]]=o;else{var a=i.replace(/(_\w)/g,(function(t){return t[1].toUpperCase()}));i!==a&&(delete t[i],t[a]=o)}}return t},ot={lines:{}},at={getByID:function(t){return t.lines}},ct={doFetchAll:function(t,e){return Object(y["a"])(regeneratorRuntime.mark((function n(){var s,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return s=t.commit,n.next=3,$.secureAxios.get("torrents/".concat(e,"/console/stdout"));case 3:i=n.sent,i.data.forEach((function(t){s(M,Object(r["a"])({torrentID:e},t))}));case 5:case"end":return n.stop()}}),n)})))()},doSocket__newLine:function(t,e){var n=t.commit,r=it(e);n(M,r)}},ut=Object(h["a"])({},M,(function(t,e){var n=e.torrentID,r=e.index,i=e.data,o=n in t.lines?t.lines[n]:[];st(o,{index:r,data:i}),s["a"].set(t.lines,n,o)})),lt={state:ot,getters:at,actions:ct,mutations:ut,namespaced:!0},dt=n("2909"),ft=(n("7db0"),n("6062"),n("3ca3"),n("ddb0"),n("99af"),n("c740"),n("6187")),pt=n.n(ft),vt=n("aced"),mt={strings:{},services:[],possible:[],isTesting:!1},bt={getStrings:function(t){return t.strings},getPossible:function(t){return t.possible},getServices:function(t){return t.services},getIsTesting:function(t){return t.isTesting},getServiceByID:function(t){return pt()(t.services,"id")},getPossibility:function(t){return function(e){return t.possible.find((function(t){return t.service_name===e}))}},getPossibleInfo:function(t,e){return function(t){var n;return null===(n=e.getPossibility(t))||void 0===n?void 0:n.setup_url}},getPossibleProtocols:function(t,e){return function(t){var n=e.getPossibility(t);return Object(dt["a"])(new Set([].concat(Object(dt["a"])(n.protocols||[]),Object(dt["a"])(n.secure_protocols||[]))))}}},gt={doPostService:function(t,e){return Object(y["a"])(regeneratorRuntime.mark((function n(){var r,s;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return r=t.commit,n.next=3,$.secureAxios.post("/notifications/services",{type:e});case 3:s=n.sent,r(G,s.data);case 5:case"end":return n.stop()}}),n)})))()},doPutServices:function(t){return Object(y["a"])(regeneratorRuntime.mark((function e(){var n,r,s,i;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=t.commit,r=t.getters,e.next=3,$.secureAxios.put("/notifications/services",{services:r.getServices});case 3:return e.next=5,n(J,!0);case 5:return e.prev=5,e.next=8,$.secureAxios.get("/notifications/test_services",r.getServices);case 8:i=e.sent,s=i.data.result,e.next=14;break;case 12:e.prev=12,e.t0=e["catch"](5);case 14:return e.prev=14,e.next=17,n(J,!1);case 17:return e.finish(14);case 18:vt["a"].open({message:s?"testing succeeded":"testing failed",type:s?"is-green":"is-primary"});case 19:case"end":return e.stop()}}),e,null,[[5,12,14,18]])})))()},doFetchServices:function(t){return Object(y["a"])(regeneratorRuntime.mark((function e(){var n,r;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=t.commit,e.next=3,$.secureAxios.get("/notifications/services");case 3:r=e.sent,n(z,r.data);case 5:case"end":return e.stop()}}),e)})))()},doFetchPossible:function(t){return Object(y["a"])(regeneratorRuntime.mark((function e(){var n,r;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=t.commit,e.next=3,$.secureAxios.get("/notifications/possible_services");case 3:r=e.sent,n(K,r.data.schemas);case 5:case"end":return e.stop()}}),e)})))()},doFetchStrings:function(t){return Object(y["a"])(regeneratorRuntime.mark((function e(){var n,r;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=t.commit,e.next=3,$.secureAxios.get("/notifications/strings");case 3:r=e.sent,n(q,r.data);case 5:case"end":return e.stop()}}),e)})))()},doPutStrings:function(t){var e=t.getters;$.secureAxios.put("/notifications/strings",e.getStrings)}},ht=(N={},Object(h["a"])(N,q,(function(t,e){s["a"].set(t,"strings",e)})),Object(h["a"])(N,V,(function(t,e){var n=e.key,r=e.value;s["a"].set(t.strings,n,r)})),Object(h["a"])(N,G,(function(t,e){t.services.push(e)})),Object(h["a"])(N,z,(function(t,e){s["a"].set(t,"services",e)})),Object(h["a"])(N,H,(function(t,e){var n=e.serviceID,r=e.key,i=e.value,o=t.services.findIndex((function(t){return t.id===n}));s["a"].set(t.services[o],r,i)})),Object(h["a"])(N,X,(function(t,e){t.services.splice(t.services.findIndex((function(t){return t.id===e})),1)})),Object(h["a"])(N,K,(function(t,e){s["a"].set(t,"possible",e)})),Object(h["a"])(N,J,(function(t,e){s["a"].set(t,"isTesting",e)})),N),_t={state:mt,getters:bt,actions:gt,mutations:ht,namespaced:!0},yt={connected:!1,systemInfo:{}},wt={getConnected:function(t){return t.connected},getSystemInfo:function(t){return t.systemInfo}},xt={doSocket__connect:function(t){var e=t.commit;e(Y,!0)},doSocket__disconnect:function(t){var e=t.commit;e(Y,!1)},doFetchSystemInfo:function(t){return Object(y["a"])(regeneratorRuntime.mark((function e(){var n,r,s;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=t.commit,e.next=3,$.secureAxios.get("/meta/system_info");case 3:r=e.sent,s=it(r.data),n(Q,s);case 6:case"end":return e.stop()}}),e)})))()}},Ct=(L={},Object(h["a"])(L,Y,(function(t,e){s["a"].set(t,"connected",e)})),Object(h["a"])(L,Q,(function(t,e){s["a"].set(t,"systemInfo",e)})),L),Ot={state:yt,getters:wt,actions:xt,mutations:Ct,namespaced:!0};s["a"].use(g["a"]);var kt=new g["a"].Store({strict:!1,modules:{torrents:nt,lines:lt,notifications:_t,status:Ot}}),St={computed:Object(g["c"])({getConnected:"status/getConnected",getSystemInfo:"status/getSystemInfo",getActiveCount:"torrents/getActiveCount",getTotal:"torrents/getTotal"}),mounted:function(){kt.dispatch("status/doFetchSystemInfo")}},Tt=St,Et=(n("fbaa"),Object(a["a"])(Tt,m,b,!1,null,"299f88df",null)),jt=Et.exports,It=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("nav",{staticClass:"navbar"},[n("div",{staticClass:"navbar-brand"},[n("router-link",{staticClass:"brand-link navbar-item",attrs:{to:"/"}},[n("img",{staticClass:"logo",attrs:{src:t.getLogoPath(),height:"100%"}})]),n("a",{staticClass:"navbar-burger",class:{"is-active":t.show},attrs:{role:"button"},on:{click:t.toggleShow}},[n("span"),n("span"),n("span")])],1),n("div",{staticClass:"navbar-menu",class:{"is-active":t.show}},[n("div",{staticClass:"navbar-end"},[n("router-link",{staticClass:"navbar-item",attrs:{to:"/torrents"}},[t._v("Torrents"),n("span",{directives:[{name:"show",rawName:"v-show",value:t.getActiveCount>0,expression:"getActiveCount > 0"}],staticClass:"activity-count"},[t._v(t._s(t.getActiveCount))])]),n("router-link",{staticClass:"navbar-item",attrs:{to:"/settings"}},[t._v("Settings")]),n("a",{staticClass:"navbar-item",on:{click:t.logout}},[n("span",[t._v("Logout ")]),n("b-icon",{attrs:{size:"is-small",icon:"logout-variant"}})],1)],1)])])},Pt=[],At={data:function(){return{show:!1}},computed:Object(r["a"])({},Object(g["c"])("torrents",["getActiveCount"])),methods:{toggleShow:function(){this.show=!this.show},getLogoPath:function(){return n("cf05")},logout:function(){w.logout()}}},Dt=At,Rt=(n("9884"),Object(a["a"])(Dt,It,Pt,!1,null,"511c9d4a",null)),Nt=Rt.exports,Lt={name:"betanin",components:{NavBar:Nt,ConnectionBanner:jt}},$t=Lt,Ft=(n("0370"),Object(a["a"])($t,p,v,!1,null,null,null)),Ut=Ft.exports,Bt=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"container"},[r("div",{staticClass:"card"},[r("img",{attrs:{id:"logo",src:n("cf05")}}),r("validation-observer",{attrs:{id:"form"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.handleSubmit;return[r("validation-provider",{attrs:{name:"username",rules:"required",slim:""},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.errors;return[r("b-field",{attrs:{type:{"is-primary":n.length},message:n[0]}},[r("b-input",{attrs:{icon:"account",placeholder:"username"},model:{value:t.username,callback:function(e){t.username=e},expression:"username"}})],1)]}}],null,!0)}),r("validation-provider",{attrs:{name:"password",rules:"required",slim:""},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.errors;return[r("b-field",{attrs:{type:{"is-primary":n.length},message:n[0]}},[r("b-input",{attrs:{icon:"lock",placeholder:"password",type:"password","password-reveal":""},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.login.apply(null,arguments)}},model:{value:t.password,callback:function(e){t.password=e},expression:"password"}})],1)]}}],null,!0)}),r("button",{staticClass:"button is-primary is-pulled-right",on:{click:function(e){return n(t.login)}}},[t._v("login")])]}}])})],1)])},Mt=[],qt=n("7bb1"),Vt={components:{ValidationProvider:qt["b"],ValidationObserver:qt["a"]},data:function(){return{username:"",password:""}},methods:{login:function(){var t=this;return Object(y["a"])(regeneratorRuntime.mark((function e(){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,w.login(t.username,t.password);case 2:if(n=e.sent,n){e.next=5;break}return e.abrupt("return");case 5:vt["a"].open({message:n,type:"is-primary"});case 6:case"end":return e.stop()}}),e)})))()}}},Kt=Vt,zt=(n("481a"),Object(a["a"])(Kt,Bt,Mt,!1,null,"5ed32f54",null)),Gt=zt.exports,Xt=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("h5",{staticClass:"title is-5"},[t._v("config.yaml")]),n("div",{staticClass:"control",class:{"is-loading":t.isLoading}},[n("textarea",{directives:[{name:"model",rawName:"v-model",value:t.text,expression:"text"}],staticClass:"textarea is-small is-info has-fixed-size",attrs:{placeholder:"hello",disabled:t.wasError},domProps:{value:t.text},on:{input:function(e){e.target.composing||(t.text=e.target.value)}}})]),t.wasError?t._e():n("p",[t._v("last read from disk at "),n("b",[t._v(t._s(t._f("formatTimestamp")(t.readAt)))])]),n("b-field",{staticClass:"buttons",attrs:{grouped:"","group-multiline":"",position:"is-right"}},[n("p",{staticClass:"control"},[n("button",{staticClass:"button is-light",on:{click:t.getConfig}},[t._v("reload")])]),n("p",{staticClass:"control"},[n("button",{staticClass:"button is-primary",attrs:{disabled:t.wasError},on:{click:t.setConfig}},[t._v("save")])])])],1)},Ht=[],Jt="/beets/config",Yt={data:function(){return{text:"",readAt:"",isLoading:null}},methods:{setConfig:function(){$.secureAxios.put(Jt,{config:this.text})},getConfig:function(){var t=this;return Object(y["a"])(regeneratorRuntime.mark((function e(){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t.isLoading=!0,e.prev=1,e.next=4,$.secureAxios.get(Jt);case 4:n=e.sent,t.text=n.data.config,t.readAt=n.data.time_read,e.next=13;break;case 9:e.prev=9,e.t0=e["catch"](1),t.text="could not load config from backend.\nreason: '".concat(e.t0.response.data.message,"'"),t.readAt=null;case 13:t.isLoading=!1;case 14:case"end":return e.stop()}}),e,null,[[1,9]])})))()}},mounted:function(){this.getConfig()},computed:{wasError:function(){return null===this.readAt}}},Qt=Yt,Wt=(n("a4f5"),Object(a["a"])(Qt,Xt,Ht,!1,null,"5ce13eac",null)),Zt=Wt.exports,te=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("b-modal",{attrs:{width:640,scroll:"keep",active:t.$route.meta.modalIsOpen,onCancel:t.openModalClose}},[n("div",{staticClass:"modal-card"},[n("header",{staticClass:"modal-card-head"},[n("p",{staticClass:"modal-card-title"},[t._v(t._s(t.torrent.name))])]),n("div",{staticClass:"console"},[n("base-console",{staticClass:"modal-card-body",attrs:{torrentID:t.torrentID,isLive:t.isLive}}),n("div",{directives:[{name:"show",rawName:"v-show",value:t.isLive,expression:"isLive"}],staticClass:"live-box"},[n("span",{staticClass:"fade"},[t._v("■")]),n("span",{staticClass:"text"},[t._v("live")])])],1),n("footer",{staticClass:"modal-card-foot"},[n("div",{staticClass:"send-input"},[n("input",{directives:[{name:"model",rawName:"v-model",value:t.stdin,expression:"stdin"},{name:"focus",rawName:"v-focus"}],staticClass:"input is-small",attrs:{type:"text",disabled:!t.isLive,placeholder:t.isLive?"send to beets":"beets has quit"},domProps:{value:t.stdin},on:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.sendStdin.apply(null,arguments)},input:function(e){e.target.composing||(t.stdin=e.target.value)}}})]),n("div",{staticClass:"send-button"},[n("button",{staticClass:"button is-small",attrs:{disabled:!t.isLive},on:{click:t.sendStdin}},[t._v("send")])])])])])},ee=[],ne=(n("caad"),function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("pre",{directives:[{name:"chat-scroll",rawName:"v-chat-scroll"}]},t._l(t.getByID[t.torrentID],(function(e){return n("p",{key:e.index,domProps:{innerHTML:t._s(t.colorLine(e.data))}})})),0)}),re=[],se=n("61ab"),ie=n.n(se),oe=new ie.a,ae={props:["torrentID","isLive"],computed:Object(r["a"])({},Object(g["c"])("lines",["getByID"])),methods:{colorLine:function(t){return oe.toHtml(t)}},mounted:function(){kt.dispatch("lines/doFetchAll",this.torrentID)}},ce=ae,ue=(n("3f21"),Object(a["a"])(ce,ne,re,!1,null,"9df53b44",null)),le=ue.exports,de={data:function(){return{stdin:""}},components:{BaseConsole:le},computed:Object(r["a"])(Object(r["a"])({},Object(g["c"])("torrents",["getTorrent"])),{},{torrentID:function(){return this.$route.params.torrentID},torrent:function(){return this.getTorrent(this.torrentID)||{}},isLive:function(){var t=this.torrent.status;return["PROCESSING","NEEDS_INPUT"].includes(t)}}),methods:{openModalClose:function(){this.$router.push({name:"torrents"})},sendStdin:function(){$.secureAxios.post("torrents/".concat(this.torrentID,"/console/stdin"),{text:this.stdin}),this.stdin=""}},mounted:function(){kt.dispatch("torrents/doFetchOne",this.torrentID)},directives:{focus:{inserted:function(t){t.focus()}}}},fe=de,pe=(n("49b9"),Object(a["a"])(fe,te,ee,!1,null,"769fe7f7",null)),ve=pe.exports,me=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("h5",{staticClass:"title is-5"},[t._v("notification format")]),n("div",{staticClass:"strings-editor"},[n("div",{staticClass:"strings-inputs"},[n("b-field",{attrs:{label:"title"}},[n("b-input",{model:{value:t.stringsTitle,callback:function(e){t.stringsTitle=e},expression:"stringsTitle"}})],1),n("b-field",{attrs:{label:"body"}},[n("b-input",{attrs:{type:"textarea"},model:{value:t.stringsBody,callback:function(e){t.stringsBody=e},expression:"stringsBody"}})],1)],1),t._m(0)]),n("div",{staticClass:"field is-pulled-right controls"},[n("button",{staticClass:"format-save-button button is-primary is-right",on:{click:function(e){return t.doPutStrings()}}},[t._v("save")])]),n("hr"),n("h5",{staticClass:"title is-5"},[t._v("services")]),n("validation-observer",{staticClass:"service-editor",scopedSlots:t._u([{key:"default",fn:function(e){var r=e.handleSubmit;return[n("h6",{directives:[{name:"show",rawName:"v-show",value:0===t.getServices.length,expression:"getServices.length === 0"}]},[n("b-icon",{attrs:{icon:"alert"}}),t._v("  no services here yet, add one below")],1),t._l(t.getServices,(function(t){return n("notification-service",{key:t.id,attrs:{serviceID:t.id}})})),n("div",{staticClass:"service-controls controls"},[n("div",{staticClass:"service-type-selector field has-addons"},[n("div",{staticClass:"control"},[n("div",{staticClass:"select is-fullwidth"},[n("select",{directives:[{name:"model",rawName:"v-model",value:t.newServiceType,expression:"newServiceType"}],on:{change:function(e){var n=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.newServiceType=e.target.multiple?n:n[0]}}},t._l(t.getPossible,(function(e){return n("option",{key:e.service_name,domProps:{value:e.service_name}},[t._v(t._s(e.service_name))])})),0)])]),n("div",{staticClass:"control"},[n("button",{staticClass:"button",on:{click:function(e){return t.doPostService(t.newServiceType)}}},[t._v("add new")])])]),n("div",{staticClass:"field"},[n("div",{staticClass:"field"},[n("div",{staticClass:"control"},[n("button",{staticClass:"button is-primary",class:{"is-loading":t.getIsTesting},on:{click:function(e){return r(t.doPutServices)}}},[t._v("save")])])])])])]}}])})],1)},be=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"variables-help"},[n("label",{staticClass:"label"},[t._v("available variables")]),n("ul",[n("li",[n("code",[t._v("$id")]),t._v(" the unique id or hash of the torrent")]),n("li",[n("code",[t._v("$title")]),t._v(" the title of the torrent")]),n("li",[n("code",[t._v("$time")]),t._v(" the timestamp of the last update to the torrent")]),n("li",[n("code",[t._v("$status")]),t._v(" the current betanin status of the torrent. eg. '"),n("b",[t._v("needs input")]),t._v("'")]),n("li",[n("code",[t._v("$console_path")]),t._v(" the relative path to the console modal")])])])}],ge=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"line"},[n("b-switch",{staticClass:"enabled-switch",model:{value:t.enabled,callback:function(e){t.enabled=e},expression:"enabled"}},[t._v(t._s(["disabled","enabled"][Number(t.service.enabled)]))]),n("div",{staticClass:"url"},[n("validation-provider",{attrs:{name:"protocol",rules:"required"},scopedSlots:t._u([{key:"default",fn:function(e){var r=e.errors;return[n("b-field",{attrs:{type:{"is-primary":r.length},message:r[0]}},[n("b-select",{staticClass:"protocol-selector",model:{value:t.protocol,callback:function(e){t.protocol=e},expression:"protocol"}},[n("option",{attrs:{disabled:"",value:""}},[t._v("please select")]),t._l(t.getPossibleProtocols(t.service.type),(function(e){return n("option",{key:e,domProps:{value:e}},[t._v(t._s(e))])}))],2)],1)]}}])}),n("p",{staticClass:"protocol-helper"},[t._v("://")]),n("validation-provider",{attrs:{name:"notProtocol",rules:"required"},scopedSlots:t._u([{key:"default",fn:function(e){var r=e.errors;return[n("b-field",{attrs:{type:{"is-primary":r.length},message:r[0]}},[n("b-input",{staticClass:"not-protocol-box",attrs:{icon:"earth",placeholder:"see info button for help"},model:{value:t.notProtocol,callback:function(e){t.notProtocol=e},expression:"notProtocol"}})],1)]}}])}),n("a",{staticClass:"info-link",attrs:{href:t.getPossibleInfo(t.service.type),target:"_blank"}},[n("b-icon",{attrs:{icon:"information",type:"is-info"}})],1)],1),n("p",{staticClass:"delete-button control"},[n("button",{staticClass:"button left-button",on:{click:function(e){return t.NOTI_SERVICE_DELETE(t.service.id)}}},[t._v("remove")])])],1)},he=[],_e=function(t){return{get:function(){var e=kt.getters["notifications/getServiceByID"],n=e[this.serviceID];return n[t]},set:function(e){kt.commit("notifications/".concat(H),{serviceID:this.serviceID,key:t,value:e})}}},ye=function(t){return{get:function(){var e=kt.getters["notifications/getStrings"];return e[t]},set:function(e){kt.commit("notifications/".concat(V),{key:t,value:e})}}},we={components:{ValidationProvider:qt["b"]},props:["serviceID"],data:function(){return{deleteIsVisible:!1}},computed:Object(r["a"])(Object(r["a"])({},Object(g["c"])("notifications",["getPossibleProtocols","getPossibleInfo"])),{},{service:function(){var t=kt.getters["notifications/getServiceByID"];return t[this.serviceID]},enabled:_e("enabled"),protocol:_e("protocol"),notProtocol:_e("not_protocol")}),methods:Object(r["a"])({},Object(g["d"])("notifications",[X]))},xe=we,Ce=(n("d19b"),Object(a["a"])(xe,ge,he,!1,null,"287f8fca",null)),Oe=Ce.exports,ke={components:{NotificationService:Oe,ValidationObserver:qt["a"]},mounted:function(){kt.dispatch("notifications/doFetchPossible"),kt.dispatch("notifications/doFetchServices"),kt.dispatch("notifications/doFetchStrings")},computed:Object(r["a"])(Object(r["a"])({},Object(g["c"])("notifications",["getServices","getPossible","getIsTesting"])),{},{stringsTitle:ye("title"),stringsBody:ye("body")}),methods:Object(r["a"])({},Object(g["b"])("notifications",["doPutStrings","doPostService","doPutServices"])),data:function(){return{newServiceType:"Kodi/XBMC"}}},Se=ke,Te=(n("3555"),Object(a["a"])(Se,me,be,!1,null,"3272ec24",null)),Ee=Te.exports,je=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("nav",{staticClass:"tabs"},[n("ul",[n("router-link",{attrs:{to:"/settings/clients",custom:""},scopedSlots:t._u([{key:"default",fn:function(e){var r=e.href,s=e.isActive;return[n("li",{class:[s&&"is-active"]},[n("a",{attrs:{href:r}},[n("b-icon",{attrs:{icon:"download"}}),t._v("torrent clients")],1)])]}}])}),n("router-link",{attrs:{to:"/settings/notifications",custom:""},scopedSlots:t._u([{key:"default",fn:function(e){var r=e.href,s=e.isActive;return[n("li",{class:[s&&"is-active"]},[n("a",{attrs:{href:r}},[n("b-icon",{attrs:{icon:"alert-circle"}}),t._v("notifications")],1)])]}}])}),n("router-link",{attrs:{to:"/settings/beets",custom:""},scopedSlots:t._u([{key:"default",fn:function(e){var r=e.href,s=e.isActive;return[n("li",{class:[s&&"is-active"]},[n("a",{attrs:{href:r}},[n("b-icon",{attrs:{icon:"note"}}),t._v("beets config")],1)])]}}])})],1)]),n("router-view")],1)},Ie=[],Pe=(n("1eb3"),{}),Ae=Object(a["a"])(Pe,je,Ie,!1,null,"25427d26",null),De=Ae.exports,Re=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("h5",{staticClass:"title is-5"},[t._v("api key")]),n("code",[t._v(t._s(t.apiKey))]),n("hr"),n("div",{staticClass:"title is-5"},[t._v("script examples")]),n("div",{staticClass:"columns"},[n("div",{staticClass:"column"},[n("div",{staticClass:"title is-7 example-heading"},[t._v("transmission")]),n("pre",[t._m(0),t._v('\n\n#!/bin/sh\n\ncurl \\\n    --request POST \\\n    --data-urlencode "path=/mnt/media/downloads" \\\n    --data-urlencode "name=$TR_TORRENT_NAME" \\\n    --header "X-API-Key: '),n("b",[t._v(t._s(t.apiKey))]),t._v('" \\\n    "'),n("b",[t._v(t._s(t.origin))]),t._v('/api/torrents"')]),n("br"),t._m(1)]),n("div",{staticClass:"column"},[n("div",{staticClass:"title is-7 example-heading"},[t._v("deluge")]),n("pre",[n("u",[t._v("# torrent-finished.sh")]),t._v('\n\n#!/bin/sh\n\ncurl \\\n    --request POST \\\n    --data-urlencode "path=/mnt/media/downloads" \\\n    --data-urlencode "name=$2" \\\n    --header "X-API-Key: '),n("b",[t._v(t._s(t.apiKey))]),t._v('" \\\n    "'),n("b",[t._v(t._s(t.origin))]),t._v('/api/torrents"')]),n("br"),t._m(2)])])])},Ne=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("u",[n("a",{attrs:{href:"https://github.com/transmission/transmission/wiki/Scripts#On_Torrent_Completion"}},[t._v("# torrent-finished.sh")])])},function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("pre",[n("u",[n("a",{attrs:{href:"https://github.com/transmission/transmission/wiki/Editing-Configuration-Files"}},[t._v("# settings.json (excerpt)")])]),t._v('\n\n...\n"script-torrent-done-enabled": '),n("b",[t._v("true")]),t._v(',\n"script-torrent-done-filename": '),n("b",[t._v('"/path/to/above/finished.sh"')]),t._v(",\n...")])},function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("p",[t._v("now install the "),n("a",{attrs:{href:"https://dev.deluge-torrent.org/wiki/Plugins/Execute#Configuration"}},[t._v("Execute")]),t._v(" plugin, and add add the above script for the event 'Torrent Complete'")])}],Le={data:function(){return{apiKey:"loading..."}},computed:{origin:function(){return window.location.origin}},mounted:function(){var t=this;return Object(y["a"])(regeneratorRuntime.mark((function e(){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,$.secureAxios.get("clients/api_key");case 2:n=e.sent,t.apiKey=n.data.api_key;case 4:case"end":return e.stop()}}),e)})))()}},$e=Le,Fe=(n("b3c2"),Object(a["a"])($e,Re,Ne,!1,null,null,null)),Ue=Fe.exports,Be=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("div",{staticClass:"manual-search"},[n("manual-import"),n("br")],1),0==t.torrents.length?n("no-active"):n("b-table",{staticClass:"torrents",attrs:{data:t.torrents,loading:t.loading,"opened-detailed":t.openedDetails,detailed:"","detail-key":"id",paginated:"","backend-pagination":"",total:t.getTotal,"per-page":t.perPage},on:{"page-change":t.onPageChange},scopedSlots:t._u([{key:"detail",fn:function(e){return[n("div",{staticClass:"row-status"},[n("p",[n("strong",[t._v("id")]),t._v(" "+t._s(e.row.id))]),n("p",[n("strong",[t._v("status")]),t._v(" "+t._s(t._f("lower")(e.row.status)))]),n("p",[n("strong",[t._v("created")]),t._v(" "+t._s(e.row.created))]),n("p",[n("strong",[t._v("updated")]),t._v(" "+t._s(e.row.updated))])])]}}])},[n("b-table-column",{attrs:{label:"name"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v(t._s(e.row.name))]}}])}),n("b-table-column",{attrs:{label:"status",numeric:!0},scopedSlots:t._u([{key:"default",fn:function(e){return[n("div",{staticClass:"controls"},[n("torrent-status",{attrs:{status:e.row.status}}),n("router-link",{directives:[{name:"show",rawName:"v-show",value:e.row.has_lines,expression:"props.row.has_lines"}],staticClass:"status-group link",attrs:{to:{name:"modal console",params:{torrentID:e.row.id}}}},[n("b-icon",{attrs:{icon:"console",size:"is-small"}}),t._v(" view")],1),["FAILED","COMPLETED"].includes(e.row.status)?n("span",{staticClass:"status-group"},[n("span",{staticClass:"link",attrs:{title:"remove torrent"},on:{click:function(n){return t.deleteTorrent(e.row.id)}}},[n("b-icon",{staticClass:"link",attrs:{icon:"close",size:"is-small"}})],1),t._v(" "),n("span",{staticClass:"link",attrs:{title:"retry import"},on:{click:function(n){return t.retryTorrent(e.row.id)}}},[n("b-icon",{staticClass:"link",attrs:{title:"retry import",icon:"refresh",size:"is-small"}})],1)]):t._e()],1)]}}])})],1),n("router-view",{attrs:{name:"modal"}})],1)},Me=[],qe=(n("d81d"),function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("div",{staticClass:"title is-6"},[n("b-icon",{attrs:{icon:"alert"}}),t._v("  there are no torrents being imported at the moment")],1),n("div",{staticClass:"title is-7 subtitle"},[t._v("make sure that you have set your torrent client up correctly")])])}),Ve=[],Ke=(n("ce70"),{}),ze=Object(a["a"])(Ke,qe,Ve,!1,null,"9ef560cc",null),Ge=ze.exports,Xe=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"search"},[n("b-field",{staticClass:"import-label",attrs:{label:"manually import"}}),n("b-field",[n("b-autocomplete",{attrs:{expanded:"",placeholder:"eg. /downloads/music/the fall - dragnet (1979)",data:t.results},on:{typing:t.manualFind},model:{value:t.selection,callback:function(e){t.selection=e},expression:"selection"}},[n("template",{slot:"empty"},[n("p",[t._v("no results found")])])],2),n("p",{staticClass:"control"},[n("button",{staticClass:"button import-button",on:{click:t.doImport}},[n("b-icon",{attrs:{icon:"folder-multiple-plus"}})],1)])],1)],1)},He=[],Je=n("f7fe"),Ye=n.n(Je),Qe={data:function(){return{results:[],selection:""}},methods:{doImport:function(){var t=this;return Object(y["a"])(regeneratorRuntime.mark((function e(){var n,r;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n="torrents",r=new FormData,r.append("both",t.selection),e.prev=3,e.next=6,$.secureAxios.post(n,r);case 6:e.next=11;break;case 8:e.prev=8,e.t0=e["catch"](3),vt["a"].open({message:"error importing: ".concat(e.t0.response.data.message),type:"is-primary"});case 11:return e.prev=11,t.selection="",e.finish(11);case 14:case"end":return e.stop()}}),e,null,[[3,8,11,14]])})))()},manualFind:Ye()(function(){var t=Object(y["a"])(regeneratorRuntime.mark((function t(e){var n,r,s,i;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(e.length){t.next=3;break}return this.results=[],t.abrupt("return");case 3:return t.next=5,$.secureAxios.get("/meta/sub_dirs",{params:{dir:e}});case 5:n=t.sent,this.results=[],r=Object(_["a"])(n.data);try{for(r.s();!(s=r.n()).done;)i=s.value,this.results.push(i.path)}catch(o){r.e(o)}finally{r.f()}case 9:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}(),200)}},We=Qe,Ze=(n("58e2"),Object(a["a"])(We,Xe,He,!1,null,"23e045ad",null)),tn=Ze.exports,en=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("span",{style:{color:t.style.colour}},[n("b-icon",{attrs:{icon:t.style.icon,size:"is-small"}}),t._v(" "+t._s(t.style.text))],1)},nn=[],rn={ENQUEUED:{text:"enqueued",icon:"clock-outline",colour:"hsl(36, 99%, 65%)"},PROCESSING:{text:"processing",icon:"clock-fast",colour:"hsl(48, 98%, 52%"},NEEDS_INPUT:{text:"needs input",icon:"alert",colour:"hsl(48, 98%, 52%)"},FAILED:{text:"failed",icon:"close",colour:"hsl(349, 58%, 57%)"},COMPLETED:{text:"completed",icon:"check",colour:"hsl(141, 71%, 48%)"}},sn={props:["status"],computed:{style:function(){return rn[this.status]}}},on=sn,an=Object(a["a"])(on,en,nn,!1,null,null,null),cn=an.exports,un={components:{ManualImport:tn,NoActive:Ge,TorrentStatus:cn},data:function(){return{page:1,perPage:25,torrentIDs:[],openedDetails:[],loading:!1}},computed:Object(r["a"])(Object(r["a"])({},Object(g["c"])("torrents",["getTorrent","getTotal"])),{},{torrents:function(){var t=this;return this.torrentIDs.map((function(e){return t.getTorrent(e)})).filter((function(t){return!!t}))}}),methods:{retryTorrent:function(t){confirm("do you want to retry this?")&&(kt.dispatch("torrents/doRetryOne",t),this.$router.push({name:"modal console",params:{torrentID:t}}))},deleteTorrent:function(t){confirm("do you want to remove this from betanin?")&&(kt.dispatch("torrents/doDeleteOne",t),this.load())},onPageChange:function(t){this.page=t,this.load()},load:function(){var t=this;return Object(y["a"])(regeneratorRuntime.mark((function e(){var n,r;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n={page:t.page,per_page:t.perPage},e.next=3,$.secureAxios.get("torrents/",{params:n});case 3:r=e.sent,t.loading=!0,kt.commit("torrents/".concat(B),{total:r.data.total,torrents:r.data.torrents}),t.torrentIDs=r.data.torrents.map((function(t){return t.id})),t.loading=!1;case 8:case"end":return e.stop()}}),e)})))()}},mounted:function(){this.load()},sockets:{newTorrent:function(t){1!==this.page||this.getTorrent(t.id)||this.torrentIDs.unshift(t.id)}}},ln=un,dn=(n("ee8c"),Object(a["a"])(ln,Be,Me,!1,null,"3af39066",null)),fn=dn.exports;s["a"].use(d["a"]);var pn=function(t,e,n){f.isLoggedIn()?n():n({name:"login",query:{redirect:t.fullPath}})},vn=[{path:"torrents",name:"torrents",component:fn,beforeEnter:pn,children:[{path:"console/:torrentID",name:"modal console",components:{modal:ve},meta:{modalIsOpen:!0}}]},{path:"settings",component:De,beforeEnter:pn,children:[{path:"clients",component:Ue},{path:"notifications",component:Ee},{path:"beets",component:Zt},{name:"settings",path:"",redirect:"clients"}]}],mn=[{name:"login",path:"/login",component:Gt},{name:"betanin",path:"/",redirect:{name:"torrents"},component:Ut,children:vn},{path:"*",redirect:"/"}],bn=new d["a"]({linkActiveClass:"is-active",routes:mn}),gn=(n("fb6a"),n("b64b"),{formatTimestamp:function(t){var e=new Date(t);return e.toLocaleTimeString("en-IE")},lower:function(t){return t.toLowerCase()},toYesNo:function(t){return t?"yes":"no"},round:function(t){return Math.round(t)},truncate:function(t,e,n){return t?t.slice(0,e)+(e<t.length?n||"...":""):""}});Object.keys(gn).forEach((function(t){s["a"].filter(t,gn[t])}));var hn=n("289d"),_n=(n("5363"),n("f87c")),yn=n("daa8"),wn=n("123d"),xn=n.n(wn),Cn=n("4c93");s["a"].config.productionTip=!1,s["a"].use(hn["a"],{defaultIconPack:"mdi",defaultContainerElement:"app"}),s["a"].use(_n["a"],Object(yn["a"])(j),{store:kt,actionPrefix:"doSocket__",mutationPrefix:"SOCKET__"}),s["a"].use(xn.a),Object(qt["c"])("required",Object(r["a"])(Object(r["a"])({},Cn["a"]),{},{message:"This field is required"}));var On=new s["a"]({router:bn,store:kt,render:function(t){return t(l)}});On.$mount("#app")},"58e2":function(t,e,n){"use strict";n("f27d")},6653:function(t,e,n){},"7beb":function(t,e,n){},"7cb8":function(t,e,n){},8475:function(t,e,n){},9511:function(t,e,n){},9884:function(t,e,n){"use strict";n("37c3")},a4f5:function(t,e,n){"use strict";n("1282")},ad5d:function(t,e,n){},ae42:function(t,e,n){},b3c2:function(t,e,n){"use strict";n("9511")},ce70:function(t,e,n){"use strict";n("ad5d")},cf05:function(t,e,n){t.exports=n.p+"img/logo.a908a471.png"},d19b:function(t,e,n){"use strict";n("8475")},da7b:function(t,e,n){},ee8c:function(t,e,n){"use strict";n("341a")},f27d:function(t,e,n){},fbaa:function(t,e,n){"use strict";n("da7b")}});
//# sourceMappingURL=app.6ef4ea44.js.map