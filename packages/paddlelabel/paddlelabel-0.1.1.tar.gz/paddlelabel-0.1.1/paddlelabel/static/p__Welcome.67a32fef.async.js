(self.webpackChunkPaddleLabel_Frontend=self.webpackChunkPaddleLabel_Frontend||[]).push([[185],{41180:function(l){l.exports={ppcard:"ppcard___27hGd",title:"title___22R8f"}},9238:function(l){l.exports={button:"button___3gM4r"}},70362:function(l){l.exports={card:"card___CFZWU",thumbnail:"thumbnail___1gIPM",button:"button___g0lkO"}},48627:function(l){l.exports={container:"container___2RXc3"}},17969:function(l){l.exports={col:"col___yKN-b"}},24141:function(l){l.exports={pagination:"pagination___1KJhU",pageSizeSelector:"pageSizeSelector___2XZ11"}},81013:function(l){l.exports={createBtn:"createBtn___UiGiR"}},75534:function(l){l.exports={table:"table___BHQO2"}},31982:function(l,E,e){"use strict";var I=e(89032),M=e(15746),D=e(11849),c=e(13062),_=e(71230),f=e(11700),i=e(67294),L=e(41180),h=e.n(L),a=e(85893),m=function(u){return(0,a.jsxs)("div",{className:h().ppcard,style:u.style,hidden:u.hidden,children:[(0,a.jsx)(_.Z,{className:h().titleRow,style:{display:u.title?void 0:"none"},children:(0,a.jsx)(f.Z,{className:h().title,children:u.title})}),(0,a.jsx)(_.Z,{style:{marginTop:26},children:(0,a.jsx)(M.Z,{span:24,style:(0,D.Z)({paddingLeft:30,paddingRight:30,textAlign:"center"},u.innerStyle),children:u.children})})]})};E.Z=m},40318:function(l,E,e){"use strict";var I=e(57663),M=e(71577),D=e(48971),c=e(67294),_=e(70362),f=e.n(_),i=e(85893),L=function(a){return(0,i.jsxs)("div",{className:f().card,style:{height:a.height,width:a.width},onClick:a.onClick?a.onClick:function(){return D.m8.push(a.href?a.href:"")},children:[(0,i.jsx)("img",{className:f().thumbnail,alt:a.wording||f().thumbnail,src:a.imgSrc,style:{height:a.height,width:a.width}}),(0,i.jsx)(M.Z,{className:f().button,style:{width:a.width},children:a.children})]})};E.Z=L},11428:function(l,E,e){"use strict";var I=e(67294),M=e(48627),D=e.n(M),c=e(85893),_=function(i){return(0,c.jsx)("div",{className:"".concat(D().container),style:{backgroundImage:"url(./pics/background.png)"},children:i.children})};E.Z=_},52940:function(l,E,e){"use strict";var I=e(11849),M=e(89032),D=e(15746),c=e(2824),_=e(67294),f=e(17969),i=e.n(f),L=e(85893),h=function(m){var U=(0,_.useState)(!1),u=(0,c.Z)(U,2),x=u[0],O=u[1];return(0,L.jsx)(D.Z,(0,I.Z)((0,I.Z)({},m),{},{className:"".concat(i().col," ").concat(m.className),style:{zIndex:x?11:10,width:"100%"},onMouseOver:function(){O(!0)},onMouseLeave:function(){O(!1)},children:m.children}))};E.Z=h},5011:function(l,E,e){"use strict";e.r(E),e.d(E,{default:function(){return ve}});var I=e(20228),M=e(11382),D=e(57663),c=e(71577),_=e(34792),f=e(48086),i=e(2824),L=e(13062),h=e(71230),a=e(89032),m=e(15746),U=e(49111),u=e(19650),x=e(67294),O=e(48971),N=e(11428),$=e(40318),b=e(31982),T=e(11849),ge=e(66456),Y=e(4421),k=e(75534),p=e.n(k),fe=e(14781),w=e(40308),je=e(43358),J=e(34041),q=e(24141),z=e.n(q),t=e(85893),A=J.Z.Option;function ee(Z){var n=Z.formatMessage({id:"component.PPTable.prev",defaultMessage:"Previous"}),P=Z.formatMessage({id:"component.PPTable.next",defaultMessage:"Next"});return function(d,r,j){return r==="prev"?(0,t.jsx)(c.Z,{children:n}):r==="next"?(0,t.jsx)(c.Z,{children:P}):j}}var te=function(n){var P=n.totalNum,d=(0,x.useState)(n.pageSize||10),r=(0,i.Z)(d,2),j=r[0],v=r[1],o=(0,x.useState)(n.currentPage||1),s=(0,i.Z)(o,2),C=s[0],R=s[1];return(0,t.jsx)("div",{className:"".concat(z().pagination),children:(0,t.jsxs)(u.Z,{align:"center",children:[(0,O.YB)().formatMessage({id:"component.PPTable.pageTotal"},{total:P,show:(0,t.jsxs)(J.Z,{value:j+"",className:z().pageSizeSelector,onChange:function(g){v(parseInt(g)),n.onChange&&n.onChange(C,parseInt(g))},children:[(0,t.jsx)(A,{value:"10",children:"10"}),(0,t.jsx)(A,{value:"20",children:"20"}),(0,t.jsx)(A,{value:"30",children:"30"}),(0,t.jsx)(A,{value:"40",children:"40"}),(0,t.jsx)(A,{value:"50",children:"50"})]})}),(0,t.jsx)(w.Z,{className:z().pagination,current:C,pageSize:j,total:P,itemRender:ee((0,O.YB)()),onChange:function(g,S){console.log("Pagination: ".concat(S,"/").concat(g)),R(g),n.onChange&&n.onChange(g,S)}})]})})},ne=te,le=function(n){var P,d=((P=n.dataSource)===null||P===void 0?void 0:P.length)||0,r=(0,x.useState)(10),j=(0,i.Z)(r,2),v=j[0],o=j[1],s=(0,x.useState)(1),C=(0,i.Z)(s,2),R=C[0],B=C[1],g=n.dataSource,S=[];if(n.dataSource){var H,F,W=v*(R-1),K=v;W+v>d&&(K=d-W+1),g=(H=n.dataSource)===null||H===void 0?void 0:H.slice(W,W+K/2),S=(F=n.dataSource)===null||F===void 0?void 0:F.slice(W+K/2,W+K)}return(0,t.jsxs)("div",{className:"".concat(p().table),children:[(0,t.jsxs)(h.Z,{children:[(0,t.jsx)(m.Z,{span:12,style:{borderRight:"0.063rem solid rgba(151,151,151,0.27)"},children:(0,t.jsx)(Y.Z,(0,T.Z)((0,T.Z)({},n),{},{dataSource:g,pagination:!1,rowSelection:void 0}))}),(0,t.jsx)(m.Z,{span:12,children:(0,t.jsx)(Y.Z,(0,T.Z)((0,T.Z)({},n),{},{dataSource:S,pagination:!1,rowSelection:void 0}))})]}),(0,t.jsx)(h.Z,{style:{marginTop:"1.75rem"},children:(0,t.jsx)(m.Z,{span:24,children:(0,t.jsx)(u.Z,{align:"center",children:(0,t.jsx)(ne,{totalNum:d,pageSize:v,currentPage:R,onChange:function(V,X){o(X),(V-1)*X>d?B(1):B(V),n.onChange&&n.onChange(V,X)}})})})})]})},ae=le,oe=e(9238),se=e.n(oe),ie=function(n){return(0,t.jsx)(c.Z,(0,T.Z)((0,T.Z)({},n),{},{style:{color:n.color,width:n.width,height:n.height,borderColor:n.color},className:"".concat(se().button),children:n.children}))},G=ie,de=e(81013),re=e.n(de),ce=function(n){return(0,t.jsx)(c.Z,{onClick:n.onClick,size:"large",id:"".concat(re().createBtn),children:n.children})},ue=ce,Pe=e(52940),y=e(15156),Q=e(36505),he=function(n){var P,d=(0,Q.I)("pages.welcome");console.log("render projects");var r=(0,y.Gd)(x.useState);(0,x.useEffect)(function(){(0,y.bo)().then(function(v){v!=!1&&r.getAll()})},[]);var j=[{title:"ID",dataIndex:"projectId",key:"projectId",width:"4.5rem",align:"center",render:function(o){return(0,t.jsx)(t.Fragment,{children:o})}},{title:"Name",dataIndex:"name",key:"projectId"},{title:"Project Category",key:"projectId",render:function(o){console.log("pj",o);var s=(0,y.os)(o.taskCategory.name);return console.log("categoryName",s),y.ux[s].name}},{title:"Actions",key:"projectId",width:"15rem",align:"center",render:function(o,s){return(0,t.jsxs)(u.Z,{size:"middle",children:[(0,t.jsx)(G,{width:"4.375rem",height:"1.875rem",color:"rgba(241,162,0,1)",onClick:function(){O.m8.push("/project_overview?projectId=".concat(s.projectId))},children:d("overview")}),(0,t.jsx)(G,{width:"4.375rem",height:"1.875rem",color:"rgba(0,100,248,1)",onClick:function(){O.m8.push("/".concat(s.taskCategory.name,"?projectId=").concat(s.projectId))},children:d("label")}),(0,t.jsx)(G,{width:"4.375rem",height:"1.875rem",color:"rgba(207,63,0,1)",onClick:function(){n.setDeleting(!0),r.remove(s).then(function(){return n.setDeleting(!1)})},children:d("remove")})]})}}];return(P=r.all)!==null&&P!==void 0&&P.length?(console.log("all pjs",(0,y.gu)(r.all)),(0,t.jsx)(h.Z,{style:{marginTop:20},children:(0,t.jsx)(m.Z,{span:24,children:(0,t.jsx)(b.Z,{title:d("myProjects"),children:(0,t.jsx)(ae,{columns:j,dataSource:(0,y.gu)(r.all),showHeader:!1})})})})):""},me=function(){var n=(0,Q.I)("pages.welcome"),P=(0,x.useState)(!1),d=(0,i.Z)(P,2),r=d[0],j=d[1];function v(){for(var o=[],s=0,C=Object.entries(y.ux);s<C.length;s++){var R=C[s],B=(0,i.Z)(R,2),g=B[0],S=B[1];o.push((0,t.jsx)(Pe.Z,{span:4,children:(0,t.jsx)($.Z,{imgSrc:S.avatar,href:"/project_detail?taskCategory="+g,onClick:g!="keypointDetection"?void 0:function(){f.default.info(n("underDevelopment","global"))},children:n(g,"global")})}))}return o}return(0,t.jsxs)(N.Z,{children:[(0,t.jsx)(h.Z,{gutter:[20,20],children:(0,t.jsx)(m.Z,{span:24,children:(0,t.jsx)(ue,{onClick:function(){O.m8.push("/sample_project")},children:n("sampleProject")})})}),(0,t.jsxs)(h.Z,{gutter:[20,20],style:{marginTop:20},children:[(0,t.jsx)(m.Z,{span:17,children:(0,t.jsx)(b.Z,{title:n("createProject"),style:{height:430},children:(0,t.jsx)(h.Z,{children:v()})})}),(0,t.jsx)(m.Z,{span:7,children:(0,t.jsx)(b.Z,{title:n("trainingKnowledge"),style:{height:430},children:(0,t.jsxs)(u.Z,{direction:"vertical",style:{width:"100%"},size:10,children:[(0,t.jsx)(c.Z,{type:"primary",style:{height:"3.125rem",lineHeight:"3.125rem"},onClick:function(){window.open("https://github.com/PaddleCV-SIG/PaddleLabel/blob/docs/doc/CN/training/PdLabel_PdClas.md")},block:!0,children:n("paddleClas")}),(0,t.jsx)(c.Z,{type:"primary",style:{height:"3.125rem",lineHeight:"3.125rem"},onClick:function(){window.open("https://github.com/PaddleCV-SIG/PaddleLabel/blob/docs/doc/CN/training/PdLabel_PdDet.md")},block:!0,children:n("paddleDet")}),(0,t.jsx)(c.Z,{type:"primary",style:{height:"3.125rem",lineHeight:"3.125rem"},onClick:function(){window.open("https://github.com/PaddleCV-SIG/PaddleLabel/blob/docs/doc/CN/training/PdLabel_PdSeg.md")},block:!0,children:n("paddleSeg")}),(0,t.jsx)(c.Z,{type:"primary",style:{height:"3.125rem",lineHeight:"3.125rem"},onClick:function(){window.open("https://github.com/PaddleCV-SIG/PaddleLabel/blob/docs/doc/CN/training/PdLabel_PdX.md")},block:!0,children:n("paddleX")})]})})})]}),(0,t.jsx)(M.Z,{tip:"Deleting",spinning:r,children:he({setDeleting:j})})]})},ve=me}}]);
