(self.webpackChunkPaddleLabel_Frontend=self.webpackChunkPaddleLabel_Frontend||[]).push([[124],{91220:function(d,i,t){"use strict";t.d(i,{Z:function(){return u}});var M=t(64254);function u(a,P){var e;if(typeof Symbol=="undefined"||a[Symbol.iterator]==null){if(Array.isArray(a)||(e=(0,M.Z)(a))||P&&a&&typeof a.length=="number"){e&&(a=e);var r=0,l=function(){};return{s:l,n:function(){return r>=a.length?{done:!0}:{done:!1,value:a[r++]}},e:function(E){throw E},f:l}}throw new TypeError(`Invalid attempt to iterate non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`)}var o=!0,c=!1,n;return{s:function(){e=a[Symbol.iterator]()},n:function(){var E=e.next();return o=E.done,E},e:function(E){c=!0,n=E},f:function(){try{!o&&e.return!=null&&e.return()}finally{if(c)throw n}}}}},41435:function(d,i,t){"use strict";t.d(i,{Z:function(){return r}});var M=t(94663),u=t(80112);function a(l){return Function.toString.call(l).indexOf("[native code]")!==-1}var P=t(18597);function e(l,o,c){return(0,P.Z)()?e=Reflect.construct:e=function(_,E,s){var m=[null];m.push.apply(m,E);var O=Function.bind.apply(_,m),f=new O;return s&&(0,u.Z)(f,s.prototype),f},e.apply(null,arguments)}function r(l){var o=typeof Map=="function"?new Map:void 0;return r=function(n){if(n===null||!a(n))return n;if(typeof n!="function")throw new TypeError("Super expression must either be null or a function");if(typeof o!="undefined"){if(o.has(n))return o.get(n);o.set(n,_)}function _(){return e(n,arguments,(0,M.Z)(this).constructor)}return _.prototype=Object.create(n.prototype,{constructor:{value:_,enumerable:!1,writable:!0,configurable:!0}}),(0,u.Z)(_,n)},r(l)}},41180:function(d){d.exports={ppcard:"ppcard___27hGd",title:"title___22R8f"}},70362:function(d){d.exports={card:"card___CFZWU",thumbnail:"thumbnail___1gIPM",button:"button___g0lkO"}},48627:function(d){d.exports={container:"container___2RXc3"}},17969:function(d){d.exports={col:"col___yKN-b"}},31982:function(d,i,t){"use strict";var M=t(89032),u=t(15746),a=t(11849),P=t(13062),e=t(71230),r=t(11700),l=t(67294),o=t(41180),c=t.n(o),n=t(85893),_=function(s){return(0,n.jsxs)("div",{className:c().ppcard,style:s.style,hidden:s.hidden,children:[(0,n.jsx)(e.Z,{className:c().titleRow,style:{display:s.title?void 0:"none"},children:(0,n.jsx)(r.Z,{className:c().title,children:s.title})}),(0,n.jsx)(e.Z,{style:{marginTop:26},children:(0,n.jsx)(u.Z,{span:24,style:(0,a.Z)({paddingLeft:30,paddingRight:30,textAlign:"center"},s.innerStyle),children:s.children})})]})};i.Z=_},40318:function(d,i,t){"use strict";var M=t(57663),u=t(71577),a=t(48971),P=t(67294),e=t(70362),r=t.n(e),l=t(85893),o=function(n){return(0,l.jsxs)("div",{className:r().card,style:{height:n.height,width:n.width},onClick:n.onClick?n.onClick:function(){return a.m8.push(n.href?n.href:"")},children:[(0,l.jsx)("img",{className:r().thumbnail,alt:n.wording||r().thumbnail,src:n.imgSrc,style:{height:n.height,width:n.width}}),(0,l.jsx)(u.Z,{className:r().button,style:{width:n.width},children:n.children})]})};i.Z=o},11428:function(d,i,t){"use strict";var M=t(67294),u=t(48627),a=t.n(u),P=t(85893),e=function(l){return(0,P.jsx)("div",{className:"".concat(a().container),style:{backgroundImage:"url(./pics/background.png)"},children:l.children})};i.Z=e},52940:function(d,i,t){"use strict";var M=t(11849),u=t(89032),a=t(15746),P=t(2824),e=t(67294),r=t(17969),l=t.n(r),o=t(85893),c=function(_){var E=(0,e.useState)(!1),s=(0,P.Z)(E,2),m=s[0],O=s[1];return(0,o.jsx)(a.Z,(0,M.Z)((0,M.Z)({},_),{},{className:"".concat(l().col," ").concat(_.className),style:{zIndex:m?11:10,width:"100%"},onMouseOver:function(){O(!0)},onMouseLeave:function(){O(!1)},children:_.children}))};i.Z=c},64873:function(d,i,t){"use strict";t.r(i);var M=t(89032),u=t(15746),a=t(13062),P=t(71230),e=t(34792),r=t(48086),l=t(67294),o=t(48971),c=t(40318),n=t(31982),_=t(11428),E=t(52940),s=t(15156),m=t(36505),O=t(85893),f=function(){var D=(0,m.I)("pages.welcome");return(0,O.jsx)(_.Z,{children:(0,O.jsx)(P.Z,{style:{marginTop:20},children:(0,O.jsx)(u.Z,{span:24,children:(0,O.jsx)(n.Z,{style:{height:500},title:D("sampleProject"),children:(0,O.jsx)(P.Z,{children:Object.entries(s.ux).map(function(h){var v=h[0],I=h[1];return(0,O.jsx)(E.Z,{span:4,children:(0,O.jsx)(c.Z,{height:360,width:310,imgSrc:I.avatar,onClick:v!="keypointDetection"?function(){s.bY.loadSample({taskCategoryId:I.id}).then(function(L){o.m8.push("/project_overview?projectId=".concat(L.projectId))})}:function(){r.default.info(D("underDevelopment","global"))},children:D(v,"global")})},v)})})})})})})};i.default=f}}]);
