(self.webpackChunkPaddleLabel_Frontend=self.webpackChunkPaddleLabel_Frontend||[]).push([[922],{41435:function(ne,M,l){"use strict";l.d(M,{Z:function(){return R}});var p=l(94663),I=l(80112);function v(S){return Function.toString.call(S).indexOf("[native code]")!==-1}var o=l(18597);function x(S,g,T){return(0,o.Z)()?x=Reflect.construct:x=function(Z,G,w){var C=[null];C.push.apply(C,G);var A=Function.bind.apply(Z,C),k=new A;return w&&(0,I.Z)(k,w.prototype),k},x.apply(null,arguments)}function R(S){var g=typeof Map=="function"?new Map:void 0;return R=function(y){if(y===null||!v(y))return y;if(typeof y!="function")throw new TypeError("Super expression must either be null or a function");if(typeof g!="undefined"){if(g.has(y))return g.get(y);g.set(y,Z)}function Z(){return x(y,arguments,(0,p.Z)(this).constructor)}return Z.prototype=Object.create(y.prototype,{constructor:{value:Z,enumerable:!1,writable:!0,configurable:!0}}),(0,I.Z)(Z,y)},R(S)}},16695:function(){},82363:function(ne,M,l){"use strict";l.d(M,{Z:function(){return Se}});var p=l(96156),I=l(90484),v=l(22122),o=l(67294),x=l(28991),R={icon:{tag:"svg",attrs:{viewBox:"64 64 896 896",focusable:"false"},children:[{tag:"path",attrs:{d:"M300 276.5a56 56 0 1056-97 56 56 0 00-56 97zm0 284a56 56 0 1056-97 56 56 0 00-56 97zM640 228a56 56 0 10112 0 56 56 0 00-112 0zm0 284a56 56 0 10112 0 56 56 0 00-112 0zM300 844.5a56 56 0 1056-97 56 56 0 00-56 97zM640 796a56 56 0 10112 0 56 56 0 00-112 0z"}}]},name:"holder",theme:"outlined"},S=R,g=l(27029),T=function(r,n){return o.createElement(g.Z,(0,x.Z)((0,x.Z)({},r),{},{ref:n,icon:S}))};T.displayName="HolderOutlined";var y=o.forwardRef(T),Z=l(76513),G=l(94184),w=l.n(G),C=l(85061),A=l(28481),k=l(23279),ve=l.n(k),ye=l(10225),re=l(1089),pe=l(86504),xe={icon:{tag:"svg",attrs:{viewBox:"64 64 896 896",focusable:"false"},children:[{tag:"path",attrs:{d:"M928 444H820V330.4c0-17.7-14.3-32-32-32H473L355.7 186.2a8.15 8.15 0 00-5.5-2.2H96c-17.7 0-32 14.3-32 32v592c0 17.7 14.3 32 32 32h698c13 0 24.8-7.9 29.7-20l134-332c1.5-3.8 2.3-7.9 2.3-12 0-17.7-14.3-32-32-32zM136 256h188.5l119.6 114.4H748V444H238c-13 0-24.8 7.9-29.7 20L136 643.2V256zm635.3 512H159l103.3-256h612.4L771.3 768z"}}]},name:"folder-open",theme:"outlined"},me=xe,ae=function(r,n){return o.createElement(g.Z,(0,x.Z)((0,x.Z)({},r),{},{ref:n,icon:me}))};ae.displayName="FolderOpenOutlined";var he=o.forwardRef(ae),Ee={icon:{tag:"svg",attrs:{viewBox:"64 64 896 896",focusable:"false"},children:[{tag:"path",attrs:{d:"M880 298.4H521L403.7 186.2a8.15 8.15 0 00-5.5-2.2H144c-17.7 0-32 14.3-32 32v592c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V330.4c0-17.7-14.3-32-32-32zM840 768H184V256h188.5l119.6 114.4H840V768z"}}]},name:"folder",theme:"outlined"},Oe=Ee,le=function(r,n){return o.createElement(g.Z,(0,x.Z)((0,x.Z)({},r),{},{ref:n,icon:Oe}))};le.displayName="FolderOutlined";var Ke=o.forwardRef(le),oe=l(65632),b;(function(e){e[e.None=0]="None",e[e.Start=1]="Start",e[e.End=2]="End"})(b||(b={}));function J(e,r){function n(a){var c=a.key,u=a.children;r(c,a)!==!1&&J(u||[],r)}e.forEach(n)}function ge(e){var r=e.treeData,n=e.expandedKeys,a=e.startKey,c=e.endKey,u=[],t=b.None;if(a&&a===c)return[a];if(!a||!c)return[];function m(f){return f===a||f===c}return J(r,function(f){if(t===b.End)return!1;if(m(f)){if(u.push(f),t===b.None)t=b.Start;else if(t===b.Start)return t=b.End,!1}else t===b.Start&&u.push(f);return n.indexOf(f)!==-1}),u}function Q(e,r){var n=(0,C.Z)(r),a=[];return J(e,function(c,u){var t=n.indexOf(c);return t!==-1&&(a.push(u),n.splice(t,1)),!!n.length}),a}var ie=function(e,r){var n={};for(var a in e)Object.prototype.hasOwnProperty.call(e,a)&&r.indexOf(a)<0&&(n[a]=e[a]);if(e!=null&&typeof Object.getOwnPropertySymbols=="function")for(var c=0,a=Object.getOwnPropertySymbols(e);c<a.length;c++)r.indexOf(a[c])<0&&Object.prototype.propertyIsEnumerable.call(e,a[c])&&(n[a[c]]=e[a[c]]);return n};function Ze(e){var r=e.isLeaf,n=e.expanded;return r?o.createElement(pe.Z,null):n?o.createElement(he,null):o.createElement(Ke,null)}function ce(e){var r=e.treeData,n=e.children;return r||(0,re.zn)(n)}var be=function(r,n){var a=r.defaultExpandAll,c=r.defaultExpandParent,u=r.defaultExpandedKeys,t=ie(r,["defaultExpandAll","defaultExpandParent","defaultExpandedKeys"]),m=o.useRef(),f=o.useRef(),D=o.createRef();o.useImperativeHandle(n,function(){return D.current});var h=function(){var d=(0,re.I8)(ce(t)),s=d.keyEntities,i;return a?i=Object.keys(s):c?i=(0,ye.r7)(t.expandedKeys||u||[],s):i=t.expandedKeys||u,i},Y=o.useState(t.selectedKeys||t.defaultSelectedKeys||[]),j=(0,A.Z)(Y,2),_=j[0],H=j[1],B=o.useState(h()),N=(0,A.Z)(B,2),E=N[0],$=N[1];o.useEffect(function(){"selectedKeys"in t&&H(t.selectedKeys)},[t.selectedKeys]),o.useEffect(function(){"expandedKeys"in t&&$(t.expandedKeys)},[t.expandedKeys]);var q=function(d,s){var i=s.isLeaf;i||d.shiftKey||d.metaKey||d.ctrlKey||D.current.onNodeExpand(d,s)},O=ve()(q,200,{leading:!0}),ee=function(d,s){var i;return"expandedKeys"in t||$(d),(i=t.onExpand)===null||i===void 0?void 0:i.call(t,d,s)},Fe=function(d,s){var i,F=t.expandAction;F==="click"&&O(d,s),(i=t.onClick)===null||i===void 0||i.call(t,d,s)},Ie=function(d,s){var i,F=t.expandAction;F==="doubleClick"&&O(d,s),(i=t.onDoubleClick)===null||i===void 0||i.call(t,d,s)},Re=function(d,s){var i,F=t.multiple,ke=s.node,P=s.nativeEvent,fe=ke.key,U=fe===void 0?"":fe,V=ce(t),W=(0,v.Z)((0,v.Z)({},s),{selected:!0}),ze=(P==null?void 0:P.ctrlKey)||(P==null?void 0:P.metaKey),je=P==null?void 0:P.shiftKey,K;F&&ze?(K=d,m.current=U,f.current=K,W.selectedNodes=Q(V,K)):F&&je?(K=Array.from(new Set([].concat((0,C.Z)(f.current||[]),(0,C.Z)(ge({treeData:V,expandedKeys:E,startKey:U,endKey:m.current}))))),W.selectedNodes=Q(V,K)):(K=[U],m.current=U,f.current=K,W.selectedNodes=Q(V,K)),(i=t.onSelect)===null||i===void 0||i.call(t,K,W),"selectedKeys"in t||H(K)},ue=o.useContext(oe.E_),we=ue.getPrefixCls,He=ue.direction,Le=t.prefixCls,Me=t.className,Te=ie(t,["prefixCls","className"]),te=we("tree",Le),Ae=w()("".concat(te,"-directory"),(0,p.Z)({},"".concat(te,"-directory-rtl"),He==="rtl"),Me);return o.createElement(se,(0,v.Z)({icon:Ze,ref:D,blockNode:!0},Te,{prefixCls:te,className:Ae,expandedKeys:E,selectedKeys:_,onSelect:Re,onClick:Fe,onDoubleClick:Ie,onExpand:ee}))},X=o.forwardRef(be);X.displayName="DirectoryTree",X.defaultProps={showIcon:!0,expandAction:"click"};var Pe=X,Ne=l(33603),Ce=l(6324),de=4;function De(e){var r,n=e.dropPosition,a=e.dropLevelOffset,c=e.prefixCls,u=e.indent,t=e.direction,m=t===void 0?"ltr":t,f=m==="ltr"?"left":"right",D=m==="ltr"?"right":"left",h=(r={},(0,p.Z)(r,f,-a*u+de),(0,p.Z)(r,D,0),r);switch(n){case-1:h.top=-3;break;case 1:h.bottom=-3;break;default:h.bottom=-3,h[f]=u+de;break}return o.createElement("div",{style:h,className:"".concat(c,"-drop-indicator")})}var z=o.forwardRef(function(e,r){var n,a=o.useContext(oe.E_),c=a.getPrefixCls,u=a.direction,t=a.virtual,m=e.prefixCls,f=e.className,D=e.showIcon,h=e.showLine,Y=e.switcherIcon,j=e.blockNode,_=e.children,H=e.checkable,B=e.selectable,N=e.draggable,E=c("tree",m),$=(0,v.Z)((0,v.Z)({},e),{showLine:Boolean(h),dropIndicatorRender:De}),q=o.useMemo(function(){if(!N)return!1;var O={};switch((0,I.Z)(N)){case"function":O.nodeDraggable=N;break;case"object":O=(0,v.Z)({},N);break;default:}return O.icon!==!1&&(O.icon=O.icon||o.createElement(y,null)),O},[N]);return o.createElement(Z.Z,(0,v.Z)({itemHeight:20,ref:r,virtual:t},$,{prefixCls:E,className:w()((n={},(0,p.Z)(n,"".concat(E,"-icon-hide"),!D),(0,p.Z)(n,"".concat(E,"-block-node"),j),(0,p.Z)(n,"".concat(E,"-unselectable"),!B),(0,p.Z)(n,"".concat(E,"-rtl"),u==="rtl"),n),f),direction:u,checkable:H&&o.createElement("span",{className:"".concat(E,"-checkbox-inner")}),selectable:B,switcherIcon:function(ee){return(0,Ce.Z)(E,Y,h,ee)},draggable:q}),_)});z.TreeNode=Z.O,z.DirectoryTree=Pe,z.defaultProps={checkable:!1,selectable:!0,showIcon:!1,motion:(0,v.Z)((0,v.Z)({},Ne.Z),{motionAppear:!1}),blockNode:!1};var se=z,Se=se},32157:function(ne,M,l){"use strict";var p=l(38663),I=l.n(p),v=l(16695),o=l.n(v)}}]);
