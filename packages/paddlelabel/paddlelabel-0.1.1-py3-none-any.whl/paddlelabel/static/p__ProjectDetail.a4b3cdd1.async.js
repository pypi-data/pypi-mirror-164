(self.webpackChunkPaddleLabel_Frontend=self.webpackChunkPaddleLabel_Frontend||[]).push([[498],{91220:function(C,x,e){"use strict";e.d(x,{Z:function(){return m}});var D=e(64254);function m(l,f){var u;if(typeof Symbol=="undefined"||l[Symbol.iterator]==null){if(Array.isArray(l)||(u=(0,D.Z)(l))||f&&l&&typeof l.length=="number"){u&&(l=u);var S=0,Z=function(){};return{s:Z,n:function(){return S>=l.length?{done:!0}:{done:!1,value:l[S++]}},e:function(i){throw i},f:Z}}throw new TypeError(`Invalid attempt to iterate non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`)}var j=!0,E=!1,h;return{s:function(){u=l[Symbol.iterator]()},n:function(){var i=u.next();return j=i.done,i},e:function(i){E=!0,h=i},f:function(){try{!j&&u.return!=null&&u.return()}finally{if(E)throw h}}}}},48627:function(C){C.exports={container:"container___2RXc3"}},18398:function(C){C.exports={_ppcard:"_ppcard___1sR0b",title:"title___2fjZe",shadow:"shadow___3SaOl",main:"main___IOVJu",block_l:"block_l___1ywNh",block_r:"block_r___Sg4L7",goup:"goup___1vznA"}},11428:function(C,x,e){"use strict";var D=e(67294),m=e(48627),l=e.n(m),f=e(85893),u=function(Z){return(0,f.jsx)("div",{className:"".concat(l().container),style:{backgroundImage:"url(./pics/background.png)"},children:Z.children})};x.Z=u},68370:function(C,x,e){"use strict";e.r(x),e.d(x,{default:function(){return w}});var D=e(34792),m=e(48086),l=e(67294),f=e(48971),u=e(20228),S=e(11382),Z=e(57663),j=e(71577),E=e(88983),h=e(47933),v=e(47673),i=e(24044),ue=e(32157),U=e(82363),ce=e(9715),g=e(93766),I=e(2824),me=e(89032),K=e(15746),F=e(11849),fe=e(13062),k=e(71230),W=e(1870),G=e(11700),Q=e(18398),P=e.n(Q),M=e(37071),r=e(15156),$=e(36505),a=e(85893),L=function(n){return(0,a.jsxs)("div",{className:P()._ppcard,style:n.style,children:[(0,a.jsxs)(k.Z,{className:P().titleRow,style:{display:n.title?void 0:"none"},children:[(0,a.jsx)(G.Z,{className:P().title,children:n.title}),(0,a.jsx)("div",{"data-test-id":n.title!=null?"projectDetailDoc":"",children:(0,a.jsx)(W.Z,{style:{fontSize:"12px"},onClick:function(){return m.default.info({content:n.content,onClick:function(){return window.open(n.docUrl)}})}})})]}),(0,a.jsx)(k.Z,{style:{marginTop:26},children:(0,a.jsx)(K.Z,{span:24,style:(0,F.Z)({paddingLeft:30,paddingRight:30,textAlign:"center"},n.innerStyle),children:n.children})})]})},J=function(n){var c=(0,r.Gd)(l.useState),y=M.Z.getQueryVariable("projectId"),q=(0,l.useState)(!1),A=(0,I.Z)(q,2),_=A[0],O=A[1],ee=(0,l.useState)([]),N=(0,I.Z)(ee,2),R=N[0],te=N[1],ae=(0,l.useState)(),V=(0,I.Z)(ae,2),ne=V[0],B=V[1],p=(0,$.I)("component.PPCreater"),o=(0,r.Ad)("component.PPCreater"),le=function(s){O(!0);var d={};s.segMaskType&&(d.segMaskType=s.segMaskType),y?c.update(y,(0,F.Z)((0,F.Z)({},s),{},{otherSettings:d})).then(function(){f.m8.push("/project_overview?projectId=".concat(y))}):c.create((0,F.Z)((0,F.Z)({},s),{},{taskCategoryId:r.ux[n.taskCategory].id,otherSettings:d})).catch(function(b){m.default.error(o("creationFail")),M.Z.parseError(b,m.default),O(!1)}).then(function(b){b&&f.m8.push("/".concat((0,r.LV)(n.taskCategory),"?projectId=").concat(b.projectId))})},re=g.Z.useForm(),se=(0,I.Z)(re,1),T=se[0];(0,l.useEffect)(function(){c.getCurr(y).then(function(t){var s,d={name:t==null?void 0:t.name,description:t==null?void 0:t.description,dataDir:t==null?void 0:t.dataDir,labelDir:t==null?void 0:t.labelDir,labelFormat:t==null?void 0:t.labelFormat,segMaskType:t==null||(s=t.otherSettings)===null||s===void 0?void 0:s.segMaskType};console.log("values",d),console.log("othersettings",t==null?void 0:t.otherSettings),t!=null&&t.labelFormat&&B(t.labelFormat),T.setFieldsValue(d)})},[]);var oe=U.Z.DirectoryTree,ie=function(s,d){console.log("Trigger Select",s,d,d.node.isLeaf!=null);var b=d.node.isLeaf!=null;b&&window.open("/api/samples/file?path="+d.node.key)};function de(){return R.length==0?(0,a.jsx)("img",{src:n.imgSrc,style:{width:"40rem"}}):(0,a.jsx)("div",{children:(0,a.jsx)(oe,{onSelect:ie,treeData:R,blockNode:!1})})}return(0,a.jsx)("div",{className:P().shadow,style:n.style,children:(0,a.jsxs)(S.Z,{tip:"Import in progress",spinning:_,children:[(0,a.jsx)("div",{id:"left",className:P().block_l,children:(0,a.jsx)(L,{title:o(n.taskCategory,"global")+o("project"),content:p("titleContent"),docUrl:"https://github.com/PaddleCV-SIG/PaddleLabel/blob/docs/doc/CN/project/".concat((0,r.LV)(n.taskCategory),".md"),style:{height:760,padding:"1.25rem 0"},children:(0,a.jsxs)(g.Z,{form:T,layout:"horizontal",size:"large",style:{marginTop:"5.69rem"},onFinish:function(s){le(s)},children:[(0,a.jsx)(g.Z.Item,{name:"name",label:o("projectName"),labelCol:{span:6},wrapperCol:{span:16},rules:[{required:!0,message:"Please input project name!"}],style:{fontSize:"1.5rem"},children:(0,a.jsx)(i.Z,{autoComplete:"off",size:"large",placeholder:o("anyString","global"),style:{height:"3.13rem"}})}),(0,a.jsx)(g.Z.Item,{name:"dataDir",label:o("datasePath"),labelCol:{span:6},wrapperCol:{span:16},rules:[{required:!0,message:"Please input dataset path!"}],style:{fontSize:"1.5rem"},children:(0,a.jsx)(i.Z,{autoComplete:"off",size:"large",placeholder:o("absolutePath","global"),style:{height:"3.13rem"},disabled:y!=null})}),(0,a.jsx)(g.Z.Item,{name:"description",label:o("description"),labelCol:{span:6},wrapperCol:{span:16},rules:[{required:!1}],style:{fontSize:"1.5rem"},children:(0,a.jsx)(i.Z,{autoComplete:"off",size:"large",placeholder:o("anyString","global"),style:{height:"3.13rem"}})}),(0,a.jsx)(g.Z.Item,{name:"labelFormat",label:o("labelFormat"),labelCol:{span:6},wrapperCol:{span:16},rules:[{required:r.ux[n.taskCategory].labelFormats!=null,message:"Please choose a label import/export format"}],style:{fontSize:"1.5rem",display:r.ux[n.taskCategory].labelFormats!=null?void 0:"none"},children:(0,a.jsx)(h.ZP.Group,{size:"large",style:{height:"3.13rem"},onChange:function(){B(T.getFieldValue("labelFormat")),r.bY.getStructure("sample/bear/".concat(n.taskCategory,"/").concat((0,r.os)(T.getFieldValue("labelFormat")),"/")).then(function(s){te(s)})},children:Object.keys(r.ux[n.taskCategory].labelFormats).map(function(t){return(0,a.jsx)(h.ZP,{value:t,children:p((0,r.os)(t),"global.labelFormat")},t)})})}),(0,a.jsx)(g.Z.Item,{name:"segMaskType",label:o("segMaskType"),labelCol:{span:6},wrapperCol:{span:16},style:{fontSize:"1.5rem",display:ne=="mask"&&n.taskCategory=="semanticSegmentation"?void 0:"none"},children:(0,a.jsx)(h.ZP.Group,{size:"large",style:{height:"3.13rem"},children:["pesudo","grayscale"].map(function(t){return(0,a.jsx)(h.ZP,{value:t,children:p(t,"global.segMaskType")},t)})})}),(0,a.jsx)(g.Z.Item,{name:"maxPoints",label:o("maxPoints"),labelCol:{span:6},wrapperCol:{span:16},rules:[{required:n.taskCategory=="keypointDetection",message:"Please input max points!"}],style:{fontSize:"1.5rem",display:n.taskCategory=="keypointDetection"?void 0:"none"},children:(0,a.jsx)(i.Z,{autoComplete:"off",size:"large",placeholder:"Numbers (Int)",style:{height:"3.13rem"}})}),(0,a.jsxs)(g.Z.Item,{wrapperCol:{span:16,offset:6},children:[(0,a.jsx)(j.Z,{htmlType:"submit",type:"primary",style:{height:"2.5rem",width:"48%"},block:!0,children:p(y?"update":"create")}),"\xA0\xA0",(0,a.jsx)(j.Z,{htmlType:"button",style:{height:"2.5rem",width:"48%"},block:!0,onClick:function(){f.m8.goBack()},children:p("cancel")})]})]})})}),(0,a.jsx)("div",{id:"right",className:P().block_r,children:(0,a.jsx)(L,{style:{height:"43.63rem",padding:"0.5rem 0"},children:de()})})]})})},H=J,X=e(11428),Y=function(){(0,r.bo)();var n=(0,r.Ad)("pages.projectDetail"),c=M.Z.getQueryVariable("taskCategory");return console.log(c),c?c in r.ux?(0,a.jsx)(X.Z,{children:(0,a.jsx)(H,{imgSrc:"./pics/illustration.jpg",taskCategory:c})}):(m.default.error(n("invalidTaskCategory")+" "+c),f.m8.push("/"),null):(m.default.error(n("noTaskCategory")),f.m8.push("/"),null)},w=Y}}]);
