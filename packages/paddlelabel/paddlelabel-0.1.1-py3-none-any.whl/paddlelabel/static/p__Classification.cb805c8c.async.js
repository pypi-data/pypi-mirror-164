(self.webpackChunkPaddleLabel_Frontend=self.webpackChunkPaddleLabel_Frontend||[]).push([[672],{41435:function(B,v,e){"use strict";e.d(v,{Z:function(){return u}});var m=e(94663),p=e(80112);function M(c){return Function.toString.call(c).indexOf("[native code]")!==-1}var h=e(18597);function s(c,a,P){return(0,h.Z)()?s=Reflect.construct:s=function(r,i,g){var O=[null];O.push.apply(O,i);var j=Function.bind.apply(r,O),D=new j;return g&&(0,p.Z)(D,g.prototype),D},s.apply(null,arguments)}function u(c){var a=typeof Map=="function"?new Map:void 0;return u=function(o){if(o===null||!M(o))return o;if(typeof o!="function")throw new TypeError("Super expression must either be null or a function");if(typeof a!="undefined"){if(a.has(o))return a.get(o);a.set(o,r)}function r(){return s(o,arguments,(0,m.Z)(this).constructor)}return r.prototype=Object.create(o.prototype,{constructor:{value:r,enumerable:!1,writable:!0,configurable:!0}}),(0,p.Z)(r,o)},u(c)}},73199:function(){},10137:function(B,v,e){"use strict";var m=e(34669),p=e(54458),M=e(67294),h=e(15156),s=e(85893),u=function(a){var P,o,r=(0,h.Ad)("pages.toolBar.progress");return(0,s.jsxs)("div",{className:"progress",children:[(0,s.jsx)(p.Z,{className:"progressBar",percent:Math.ceil(a.project.finished/((P=a.task.all)===null||P===void 0?void 0:P.length)*100),status:"active",showInfo:!1})," ",(0,s.jsx)("span",{className:"progressDesc",children:"".concat(r(""),": ").concat(a.project.finished||0,"/").concat((o=a.task.all)===null||o===void 0?void 0:o.length,`
        `).concat(r("currentId"),": ").concat(a.task.currIdx==null?1:a.task.currIdx+1," ")})]})};v.Z=u},29214:function(B,v,e){"use strict";e.r(v);var m=e(11849),p=e(20228),M=e(11382),h=e(34792),s=e(48086),u=e(91220),c=e(67294),a=e(48971),P=e(73199),o=e.n(P),r=e(8088),i=e(61541),g=e(44434),O=e(5041),j=e(57436),D=e(10137),K=e(15156),U=e(36505),t=e(85893),Z=function(){var l=(0,K.$L)(c.useState,c.useEffect,{label:{oneHot:!1,postSelect:k},tool:{defaultTool:"mover"},effectTrigger:{postTaskChange:N,postProjectChanged:S}}),T=l.tool,A=l.loading,b=l.scale,f=l.annotation,I=l.task,R=l.data,L=l.project,_=l.label,y=l.refreshVar,d=(0,U.I)("pages.toolBar");function S(){var n;((n=L.curr)===null||n===void 0?void 0:n.labelFormat)=="single_class"&&_.setOneHot(!0)}function k(n,E){if(console.log("selectLabel",n),E.has(n.labelId))_.isOneHot&&f.clear(),f.create({taskId:I.curr.taskId,labelId:n.labelId,dataId:R.curr.dataId});else{var F=f.all.filter(function(x){return x.labelId==n.labelId}),C=(0,u.Z)(F),W;try{for(C.s();!(W=C.n()).done;){var $=W.value;f.remove($.annotationId)}}catch(x){C.e(x)}finally{C.f()}}}function N(n,E){A.setCurr(!0),!(!n||!E)&&(_.initActive(E),A.setCurr(!1))}return(0,t.jsxs)(r.Z,{className:o().classes,children:[(0,t.jsxs)(g.Z,{children:[(0,t.jsx)(i.Z,{imgSrc:"./pics/buttons/zoom_in.png",onClick:function(){b.change(.1)},children:d("zoomIn")}),(0,t.jsx)(i.Z,{imgSrc:"./pics/buttons/zoom_out.png",onClick:function(){b.change(-.1)},children:d("zoomOut")}),(0,t.jsx)(i.Z,{imgSrc:"./pics/buttons/save.png",onClick:function(){s.default.success(d("autoSave"))},children:d("save")}),(0,t.jsx)(i.Z,{imgSrc:"./pics/buttons/move.png",active:T.curr=="mover",onClick:function(){T.setCurr("mover")},children:d("move")}),(0,t.jsx)(i.Z,{imgSrc:"./pics/buttons/clear_mark.png",onClick:function(){f.clear()},children:d("clearMark")})]}),(0,t.jsx)("div",{id:"dr",className:"mainStage",children:(0,t.jsxs)(M.Z,{tip:d("loading","global"),spinning:A.curr,children:[(0,t.jsx)("div",{className:"draw",children:(0,t.jsx)(j.Z,{scale:b.curr,currentTool:T.curr,setCurrentAnnotation:function(){},onAnnotationModify:function(){},onAnnotationModifyComplete:function(){},imgSrc:R.imgSrc,annotations:f.all})}),(0,t.jsx)("div",{className:"pblock",children:(0,t.jsx)(D.Z,{task:I,project:L})}),(0,t.jsx)("div",{className:"prevTask",onClick:I.prevTask,"data-test-id":"prevTask"}),(0,t.jsx)("div",{className:"nextTask",onClick:I.nextTask,"data-test-id":"nextTask"})]})}),(0,t.jsx)(g.Z,{disLoc:"right",children:(0,t.jsx)(i.Z,{imgSrc:"./pics/buttons/data_division.png",onClick:function(){a.m8.push("/project_overview?projectId=".concat(L.curr.projectId))},children:d("projectOverview")})}),(0,t.jsx)("div",{className:"rightSideBar",children:(0,t.jsx)(O.Z,{labels:_.all,activeIds:_.activeIds,onLabelSelect:_.onSelect,onLabelAdd:function(E){return _.create((0,m.Z)((0,m.Z)({},E),{},{projectId:L.curr.projectId}))},onLabelDelete:_.remove,hideColorPicker:!0,hideEye:!0,refresh:y})})]})};v.default=Z}}]);
