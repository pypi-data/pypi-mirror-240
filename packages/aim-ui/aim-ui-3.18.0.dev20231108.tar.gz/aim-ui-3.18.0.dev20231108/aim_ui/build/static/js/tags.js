(this.webpackJsonpui_v2=this.webpackJsonpui_v2||[]).push([[37],{1497:function(e,t,a){},645:function(e,t,a){"use strict";a.r(t);var n,i,o=a(0),c=a.n(o),r=a(278),l=a(12),s=a(18),d=a(2),u=a(8),g=a.n(u),j=a(27),m=a(6),b=a(338),v=a(280),f=Object(v.a)({isTagsDataLoading:!1,isRunsDataLoading:!1,isTagInfoDataLoading:!1,notifyData:[]});function h(e){var t,a=(null===(t=f.getState())||void 0===t?void 0:t.notifyData)||[];a=Object(m.a)(a).filter((function(t){return t.id!==e})),f.setState({notifyData:a})}function O(e){var t,a=(null===(t=f.getState())||void 0===t?void 0:t.notifyData)||[];a=[].concat(Object(m.a)(a),[e]),f.setState({notifyData:a}),setTimeout((function(){h(e.id)}),3e3)}var _=Object(d.a)(Object(d.a)({},f),{},{initialize:function(){f.init()},getTagsData:function(){var e=b.a.getTags(),t=e.call;return{call:function(){f.setState({isTagsDataLoading:!0}),t().then((function(e){f.setState({tagsList:e,isTagsDataLoading:!1})}))},abort:e.abort}},getTagRuns:function(e){var t,a;return n&&(null===(a=n)||void 0===a||a.abort()),n=b.a.getTagRuns(e),{call:function(){var e=Object(j.a)(g.a.mark((function e(){var t;return g.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return f.setState({isRunsDataLoading:!0}),e.next=3,n.call();case 3:t=e.sent,f.setState({tagRuns:t.runs,isRunsDataLoading:!1});case 5:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),abort:null===(t=n)||void 0===t?void 0:t.abort}},archiveTag:function(e){var t=arguments.length>1&&void 0!==arguments[1]&&arguments[1],a=f.getState();return b.a.hideTag(e,t).call().then((function(){f.setState(Object(d.a)(Object(d.a)({},a),{},{tagInfo:Object(d.a)(Object(d.a)({},null===a||void 0===a?void 0:a.tagInfo),{},{archived:t})})),O({id:Date.now(),severity:"success",messages:[t?"Tag successfully archived":"Tag successfully unarchived"]})}))},getTagById:function(e){var t,a;return i&&(null===(a=i)||void 0===a||a.abort()),i=b.a.getTagById(e),{call:function(){var e=Object(j.a)(g.a.mark((function e(){var t;return g.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return f.setState({isTagInfoDataLoading:!0}),e.next=3,i.call();case 3:t=e.sent,f.setState({tagInfo:t,isTagInfoDataLoading:!1});case 5:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),abort:null===(t=i)||void 0===t?void 0:t.abort}},updateTagInfo:function(e){var t=f.getState();f.setState(Object(d.a)(Object(d.a)({},t),{},{tagInfo:e}))},onNotificationDelete:h,deleteTag:function(e){return b.a.deleteTag(e).call().then((function(){O({id:Date.now(),severity:"success",messages:["Tag successfully deleted"]})}))},createTag:function(e){return b.a.createTag(e).call().then((function(e){return e.id?O({id:Date.now(),severity:"success",messages:["Tag successfully created"]}):O({id:Date.now(),severity:"error",messages:[e.detail]}),e}))},updateTag:function(e,t){return b.a.updateTag(e,t).call().then((function(e){return e.id?O({id:Date.now(),severity:"success",messages:["Tag successfully updated"]}):O({id:Date.now(),severity:"error",messages:[e.detail]}),e}))}}),x=a(15),T=a(7),p=a(410),y=a(1589),C=a(1579),D=a(711),N=a(209),w=a(1);function L(e){var t=e.children,a=e.value,n=e.index,i=e.className;return Object(w.jsx)(N.a,{children:Object(w.jsx)("div",{role:"tabpanel",hidden:a!==n,id:"wrapped-tabpanel-".concat(n),"aria-labelledby":"wrapped-tab-".concat(n),className:i,children:a===n&&Object(w.jsx)(D.a,{children:t})})})}var I=Object(o.memo)(L),S=a(738),F=a(705),R=a(696),k=a(698),B=a(713),M=a(974),z=a(227),P=a(443),H=a(975),E=a(3),A=a(463),V=a(221);var K=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};return Object(A.a)(e,Object(E.a)({defaultTheme:V.a},t))},U=a(5),Z=a(31),q=(a(1497),K({tagColor:{border:function(e){var t=e.colorName,a=e.color;return"1px solid ".concat(t===a?a:"transparent")},"&:hover, &:focus":{border:function(e){var t=e.colorName;return"1px solid ".concat(t," !important;")},backgroundColor:"inherit"}}}));function G(e){var t=e.colorName,a=e.onColorButtonClick,n=e.color,i=q({color:n,colorName:t}).tagColor;return Object(w.jsx)(R.a,{className:"TagForm__tagFormContainer__colorContainer__colorBox__colorButton ".concat(i),onClick:function(){return a(t)},children:Object(w.jsxs)(w.Fragment,{children:[Object(w.jsx)("span",{className:"TagForm__tagFormContainer__colorContainer__colorBox__colorButton__content",style:{background:t}}),Object(w.jsx)("span",{className:"TagForm__tagFormContainer__colorContainer__colorBox__colorButton__circle",style:{background:t}})]})})}function J(e){var t=e.tagData,a=e.editMode,n=e.tagId,i=e.onCloseModal,c=Object(H.a)({initialValues:a?{name:(null===t||void 0===t?void 0:t.name)||"",color:(null===t||void 0===t?void 0:t.color)||Z.d[0][0],comment:(null===t||void 0===t?void 0:t.description)||""}:{name:"",color:Z.d[0][0],comment:""},onSubmit:z.a,validationSchema:M.a({name:M.b().required("Required field").max(50,"Must be 50 characters or fewer"),comment:M.b().max(100,"Must be 100 characters or fewer")})}),r=c.values,d=c.errors,u=c.touched,g=c.setFieldValue,j=c.setValues,m=c.setFieldTouched,b=c.submitForm,v=c.validateForm,f=r.name,h=r.color,O=r.comment;function T(e,t){var a;g(t,null===e||void 0===e||null===(a=e.target)||void 0===a?void 0:a.value,!0).then((function(){m(t,!0)}))}var p=Object(o.useMemo)((function(){return Z.d[0].map((function(e,t){return Object(w.jsx)(G,{color:h,colorName:e,onColorButtonClick:y},e)}))}),[h]);function y(e){g("color",e)}return Object(w.jsx)(l.a,{children:Object(w.jsxs)("div",{className:"TagForm",children:[Object(w.jsxs)("div",{className:"TagForm__tagFormContainer",children:[Object(w.jsx)(U.n,{component:"p",tint:60,children:"Name"}),Object(w.jsx)(F.a,{placeholder:"Name",variant:"outlined",className:"TagForm__tagFormContainer__TextField TextField__OutLined__Medium",onChange:function(e){return T(e,"name")},value:f,size:"small",error:!(!u.name||!d.name),helperText:u.name&&d.name}),Object(w.jsx)(U.n,{component:"p",tint:60,children:"Comment"}),Object(w.jsx)(F.a,{placeholder:"Comment",variant:"outlined",onChange:function(e){return T(e,"comment")},className:"TagForm__tagFormContainer__TextField TextField__TextArea__OutLined__Small",multiline:!0,value:O,error:!(!u.comment||!d.comment),helperText:u.comment&&d.comment}),Object(w.jsxs)("div",{className:"TagForm__tagFormContainer__colorContainer",children:[Object(w.jsx)(U.n,{component:"p",tint:50,children:"Colors"}),Object(w.jsx)("div",{className:"TagForm__tagFormContainer__colorContainer__colorBox",children:p})]}),Object(w.jsxs)("div",{className:"TagForm__tagFormContainer__previewContainer",children:[Object(w.jsx)(U.n,{component:"p",tint:30,children:"Preview"}),Object(w.jsx)("div",{className:"TagForm__tagFormContainer__previewContainer__tagPreviewBox",children:Object(w.jsx)(U.b,{label:f||"Tag Preview",color:h})})]})]}),Object(w.jsxs)("div",{className:"TagForm__tagFormFooterContainer",children:[Object(w.jsx)(R.a,{onClick:a?function(){j({name:(null===t||void 0===t?void 0:t.name)||"",color:(null===t||void 0===t?void 0:t.color)||"",comment:(null===t||void 0===t?void 0:t.description)||""},!0)}:i,className:"TagForm__tagFormFooterContainer__cancelButton",color:"secondary",children:a?"Reset":"Cancel"}),Object(w.jsx)(R.a,{onClick:a?function(){b().then((function(){return v(r).then((function(e){Object(P.a)(e)&&_.updateTag({name:f,color:h,description:O},n||"").then((function(){_.getTagsData().call(),_.getTagById(n||"").call(),i()}))}))}))}:function(){Object(x.b)(s.a.tags.create),b().then((function(){return v(r).then((function(e){Object(P.a)(e)&&_.createTag({name:f,color:h,description:O}).then((function(e){e.id&&(i(),_.getTagsData().call())}))}))}))},variant:"contained",color:"primary",children:a?"Save":"Create"})]})]})})}var W=Object(o.memo)(J),Q=a(69),X=a(376),Y=a(196);function $(e){var t=e.tableRef,a=e.tagsList,n=e.hasSearchValue,i=e.isTagsDataLoading,c=e.onTableRunClick,r=e.onSoftDeleteModalToggle,s=e.onUpdateModalToggle,d=e.onDeleteModalToggle,u=Object(o.useState)(""),g=Object(T.a)(u,2),j=g[0],m=g[1],b=[{dataKey:"name",key:"name",title:"Name & Color",width:200,cellRenderer:function(e,t){var a=e.cellData,n=a.name,i=a.color;return Object(w.jsx)(U.b,{label:n,color:i,maxWidth:"100%"},t)}},{dataKey:"runs",key:"runs",title:"Runs",width:150,cellRenderer:function(e,t){var a=e.cellData;return Object(w.jsxs)("div",{className:"TagsTable__runsCell",children:[Object(w.jsx)("span",{className:"TagsTable__runsCell--iconBox",children:Object(w.jsx)(U.f,{name:"circle-with-dot"})}),Object(w.jsx)(U.n,{size:14,color:"info",children:a.count})]})}},{dataKey:"comment",key:"comment",title:"Comment",width:0,flexGrow:1,cellRenderer:function(e){var t=e.cellData;e.i;return Object(w.jsxs)("div",{className:"TagsTable__commentCell",role:"button","aria-pressed":"false",onClick:function(e){return e.stopPropagation()},children:[Object(w.jsx)(U.n,{size:14,tint:100,children:t.description}),t.id===j&&Object(w.jsxs)("div",{className:"TagsTable__commentCell__actionsContainer",children:[!(null===t||void 0===t?void 0:t.archived)&&Object(w.jsx)(U.c,{withOnlyIcon:!0,onClick:function(){return e=t,_.updateTagInfo(e),void s();var e},children:Object(w.jsx)(U.f,{color:"primary",name:"edit"})}),(null===t||void 0===t?void 0:t.archived)?Object(w.jsx)(U.c,{withOnlyIcon:!0,onClick:function(){return v(t)},children:Object(w.jsx)(U.f,{color:"primary",name:"eye-show-outline"})}):Object(w.jsx)(U.c,{withOnlyIcon:!0,onClick:function(){return v(t)},children:Object(w.jsx)(U.f,{color:"primary",name:"eye-outline-hide"})}),Object(w.jsx)(U.c,{onClick:function(){return e=t,_.updateTagInfo(e),void d();var e},withOnlyIcon:!0,children:Object(w.jsx)(U.f,{fontSize:"small",name:"delete",color:"primary"})})]})]})}}];function v(e){_.updateTagInfo(e),r()}return Object(o.useEffect)((function(){var e;t.current.updateData&&(null===t||void 0===t||null===(e=t.current)||void 0===e||e.updateData({newData:a.map((function(e,t){return{key:e.id,name:{name:e.name,color:e.color},comment:e,runs:{count:e.run_count,tagId:e.id}}})),newColumns:b}))}),[a,c,j]),Object(w.jsx)(l.a,{children:Object(w.jsxs)("div",{className:"Tags__TagList__tagListBox",children:[Object(w.jsx)("div",{className:"Tags__TagList__tagListBox__titleBox",children:!i&&!Q.a.isNil(a)&&Object(w.jsxs)(U.n,{component:"h4",size:14,weight:600,tint:100,children:[a.length," ",a.length>1?"Tags":"Tag"]})}),Object(w.jsx)(X.a,{ref:t,fixed:!1,columns:b,data:null,isLoading:i,hideHeaderActions:!0,rowHeight:52,headerHeight:32,onRowHover:function(e){return m(e)},onRowClick:function(e){return c(e||"")},illustrationConfig:{type:n?Y.c.EmptySearch:Y.c.ExploreData,page:"tags"},height:"calc(100% - 39px)"})]})})}var ee=Object(o.memo)($),te=a(279),ae=a(369),ne=a(140),ie=a(74),oe=a.n(ie),ce=a(351),re=a(384),le=a(82),se=a(166);function de(e){var t=e.runsList,a=Object(o.useRef)({}),n=[{dataKey:"name",key:"name",title:"Name",width:0,flexGrow:1,cellRenderer:function(e){var t=e.cellData;return Object(w.jsxs)(w.Fragment,{children:[Object(w.jsx)(ce.a,{title:t.active?"In Progress":"Finished",children:Object(w.jsx)("div",{children:Object(w.jsx)(re.a,{className:"Table__status_indicator",status:t.active?"success":"alert"})})}),Object(w.jsx)(ce.a,{title:t.name,children:Object(w.jsx)("div",{children:Object(w.jsx)(ne.c,{to:"/runs/".concat(t.id),children:Object(w.jsx)("p",{className:"TagsTable__runName",children:t.name})})})})]})}},{dataKey:"date",key:"date",title:"Date",width:200,cellRenderer:function(e){var t=e.cellData;return Object(w.jsx)("p",{className:"TagsTable__runCreatedDate",children:t})}},{dataKey:"duration",key:"duration",title:"Duration",width:200,cellRenderer:function(e){var t=e.cellData;return Object(w.jsx)("p",{className:"TagsTable__runDuration",children:t})}}];return Object(o.useEffect)((function(){var e;t&&(null===a||void 0===a||null===(e=a.current)||void 0===e||e.updateData({newData:t.map((function(e){return{name:{name:e.name,id:e.run_id,active:Q.a.isNil(e.end_time)},date:oe()(1e3*e.creation_time).format(le.f),duration:Object(se.a)(1e3*e.creation_time,e.end_time?1e3*e.end_time:Date.now()),key:e.run_id}})),newColumns:n}))}),[t]),Object(w.jsx)(l.a,{children:Object(w.jsx)("div",{className:"TagsTable",children:Object(w.jsx)(X.a,{ref:a,fixed:!1,columns:n,data:[],hideHeaderActions:!0,rowHeight:32,headerHeight:32,height:"calc(100% - 10px)",disableRowClick:!0})})})}var ue=Object(o.memo)(de);a(859);function ge(e){var t=e.id,a=e.onSoftDeleteModalToggle,n=e.onUpdateModalToggle,i=e.onDeleteModalToggle,c=e.isTagInfoDataLoading,r=e.tagInfo,s=e.isRunsDataLoading,d=e.tagRuns;return Object(o.useEffect)((function(){var e=_.getTagById(t),a=_.getTagRuns(t);return a.call(),e.call(),function(){a.abort(),e.abort()}}),[t]),Object(w.jsx)(l.a,{children:Object(w.jsxs)("div",{className:"TagDetail",children:[Object(w.jsxs)("div",{className:"TagDetail__headerContainer",children:[Object(w.jsx)(te.a,{isLoading:c,loaderType:"skeleton",loaderConfig:{variant:"rect",width:100,height:24},width:"auto",children:r&&Object(w.jsx)(U.b,{size:"medium",color:null===r||void 0===r?void 0:r.color,label:null===r||void 0===r?void 0:r.name})}),Object(w.jsxs)("div",{className:"TagDetail__headerContainer__headerActionsBox",children:[!(null===r||void 0===r?void 0:r.archived)&&Object(w.jsx)(U.c,{withOnlyIcon:!0,onClick:n,children:Object(w.jsx)(U.f,{name:"edit"})}),(null===r||void 0===r?void 0:r.archived)?Object(w.jsx)(U.c,{onClick:a,withOnlyIcon:!0,children:Object(w.jsx)(U.f,{name:"eye-show-outline",color:"primary"})}):Object(w.jsx)(U.c,{withOnlyIcon:!0,onClick:a,children:Object(w.jsx)(U.f,{name:"eye-outline-hide",color:"primary"})}),Object(w.jsx)(U.c,{withOnlyIcon:!0,onClick:i,children:Object(w.jsx)(U.f,{name:"delete",fontSize:"small",color:"primary"})})]})]}),Object(w.jsx)(te.a,{isLoading:s,className:"Tags__TagList__tagListBusyLoader",children:Object(P.a)(d)?Object(w.jsx)(ae.a,{size:"xLarge",title:"No Runs"}):Object(w.jsx)(ue,{runsList:d})})]})})}var je=Object(o.memo)(ge),me=a(734);function be(e){var t,a,n,i,c=e.tagInfo,r=e.tagHash,s=e.onSoftDeleteModalToggle,d=e.onTagDetailOverlayToggle,u=e.isTagDetailOverLayOpened,g=e.modalIsOpen,j=Object(o.useRef)({archived:null===c||void 0===c?void 0:c.archived});return Object(w.jsx)(l.a,{children:Object(w.jsx)(me.a,{open:g,onCancel:s,onSubmit:(null===(t=j.current)||void 0===t||t.archived,function(){_.archiveTag(r,!(null===c||void 0===c?void 0:c.archived)).then((function(){_.getTagsData().call(),s(),u&&d()}))}),text:"Are you sure you want to ".concat((null===(a=j.current)||void 0===a?void 0:a.archived)?"bring back":"hide"," this tag?"),icon:Object(w.jsx)(U.f,{name:(null===(n=j.current)||void 0===n?void 0:n.archived)?"eye-show-outline":"eye-outline-hide"}),title:"Hide tag",confirmBtnText:(null===(i=j.current)||void 0===i?void 0:i.archived)?"Bring back":"Hide"})})}var ve=Object(o.memo)(be);function fe(e){var t=e.tagInfo,a=e.tagHash,n=e.onDeleteModalToggle,i=e.onTagDetailOverlayToggle,o=e.isTagDetailOverLayOpened,c=e.modalIsOpen,r=Object(H.a)({initialValues:{name:""},onSubmit:z.a,validationSchema:M.a({name:M.b().test("name","Name does not match",(function(e){return e===t.name}))})}),s=r.values,d=r.errors,u=r.touched,g=r.setFieldValue,j=r.setFieldTouched,m=r.submitForm,b=r.validateForm,v=s.name;function f(){g("name",""),j("name",!1),n()}return Object(w.jsx)(l.a,{children:Object(w.jsxs)(me.a,{open:c,onCancel:f,onSubmit:function(){m().then((function(){return b(s).then((function(e){Object(P.a)(e)&&_.deleteTag(a).then((function(){_.getTagsData().call(),o&&i(),f()}))}))}))},text:"Are you sure you want to delete this tag?",icon:Object(w.jsx)(U.f,{name:"delete"}),title:"Delete tag",statusType:"error",confirmBtnText:"Delete",children:[Object(w.jsx)(U.n,{component:"p",weight:400,tint:100,className:"TagDelete__contentContainer__contentBox__warningText",children:'Please type "'.concat(null===t||void 0===t?void 0:t.name,'" to confirm:')}),Object(w.jsx)(F.a,{label:"Name",value:v,id:"name",variant:"outlined",className:"TagForm__tagFormContainer__labelField TextField__OutLined__Small",size:"small",onChange:function(e){var t;g("name",null===e||void 0===e||null===(t=e.target)||void 0===t?void 0:t.value,!0).then((function(){j("name",!0)}))},error:!(!u.name||!d.name),helperText:u.name&&d.name})]})})}var he=Object(o.memo)(fe);function Oe(e){var t=e.tagsList,a=e.isHiddenTagsList,n=e.isTagsDataLoading,i=e.tagInfo,c=e.tagRuns,r=e.isRunsDataLoading,d=e.isTagInfoDataLoading,u=Object(o.useRef)({}),g=Object(o.useState)(!1),j=Object(T.a)(g,2),m=j[0],b=j[1],v=Object(o.useState)(!1),f=Object(T.a)(v,2),h=f[0],O=f[1],_=Object(o.useState)(!1),p=Object(T.a)(_,2),y=p[0],C=p[1],D=Object(o.useState)(!1),N=Object(T.a)(D,2),L=N[0],I=N[1],S=Object(o.useState)(!1),M=Object(T.a)(S,2),z=M[0],P=M[1],H=Object(o.useState)(""),E=Object(T.a)(H,2),A=E[0],V=E[1],K=Object(o.useState)(""),Z=Object(T.a)(K,2),q=Z[0],G=Z[1];function J(){b(!m)}function Q(){O(!h)}function X(){C(!y)}function Y(){I(!L)}function $(){var e;z&&(null===(e=u.current)||void 0===e||e.setActiveRow(null));P(!z)}return Object(w.jsxs)("div",{className:"Tags__TagList",children:[Object(w.jsxs)("div",{className:"Tags__TagList__header",children:[Object(w.jsx)(F.a,{placeholder:"Search",variant:"outlined",InputProps:{startAdornment:Object(w.jsx)(U.f,{name:"search"}),disabled:n},onChange:function(e){G(e.target.value)},value:q}),!a&&Object(w.jsxs)(R.a,{variant:"contained",size:"small",className:"Tags__TagList__header__createButton",color:"primary",onClick:J,children:[Object(w.jsx)(U.f,{name:"plus"}),"Create Tag"]})]}),Object(w.jsxs)(l.a,{children:[Object(w.jsx)(ee,{tableRef:u,tagsList:t.filter((function(e){return e.name.includes(q)})),isTagsDataLoading:n,hasSearchValue:!!q,onTableRunClick:function(e){z||P(!0),V(e),x.b(s.a.tags.tagDetail)},onSoftDeleteModalToggle:X,onDeleteModalToggle:Y,onUpdateModalToggle:Q}),Object(w.jsx)(k.a,{onClose:J,"aria-labelledby":"customized-dialog-title",open:m,children:Object(w.jsxs)("div",{className:"Tags__TagList__modalContainer",children:[Object(w.jsx)("div",{className:"Tags__TagList__modalContainer__titleBox",children:Object(w.jsx)(U.n,{component:"h4",weight:600,tint:100,size:14,children:"Create Tag"})}),Object(w.jsx)("div",{className:"Tags__TagList__modalContainer__contentBox",children:Object(w.jsx)(W,{onCloseModal:J})})]})},(null===i||void 0===i?void 0:i.id)+"1"),Object(w.jsx)(k.a,{onClose:Q,"aria-labelledby":"customized-dialog-title",open:h,children:Object(w.jsxs)("div",{className:"Tags__TagList__modalContainer",children:[Object(w.jsx)("div",{className:"Tags__TagList__modalContainer__titleBox",children:Object(w.jsx)(U.n,{component:"h4",size:14,tint:100,weight:600,children:"Update Tag"})}),Object(w.jsx)("div",{className:"Tags__TagList__modalContainer__contentBox",children:Object(w.jsx)(W,{onCloseModal:Q,tagData:i,tagId:null===i||void 0===i?void 0:i.id,editMode:!0})})]})},(null===i||void 0===i?void 0:i.id)+"2"),i&&Object(w.jsx)(ve,{modalIsOpen:y,tagInfo:i,tagHash:null===i||void 0===i?void 0:i.id,onSoftDeleteModalToggle:X,onTagDetailOverlayToggle:$,isTagDetailOverLayOpened:z}),i&&Object(w.jsx)(he,{modalIsOpen:L,tagInfo:i,tagHash:null===i||void 0===i?void 0:i.id,onDeleteModalToggle:Y,onTagDetailOverlayToggle:$,isTagDetailOverLayOpened:z},null===i||void 0===i?void 0:i.id)]}),Object(w.jsx)(B.a,{className:"Tags__TagList__overLayContainer",anchor:"right",open:z,onClose:$,children:z&&Object(w.jsx)(je,{id:A,onSoftDeleteModalToggle:X,onUpdateModalToggle:Q,onDeleteModalToggle:Y,tagRuns:c,tagInfo:i,isRunsDataLoading:r,isTagInfoDataLoading:d})})]})}var _e=Object(o.memo)(Oe);function xe(e){var t=e.tagsListData,a=e.isTagsDataLoading,n=e.tagInfo,i=e.tagRuns,c=e.onNotificationDelete,r=e.notifyData,d=e.isRunsDataLoading,u=e.isTagInfoDataLoading,g=Object(o.useState)(0),j=Object(T.a)(g,2),m=j[0],b=j[1],v=Object(o.useState)((null===t||void 0===t?void 0:t.filter((function(e){return e.archived})))||[]),f=Object(T.a)(v,2),h=f[0],O=f[1],_=Object(o.useState)((null===t||void 0===t?void 0:t.filter((function(e){return!e.archived})))||[]),D=Object(T.a)(_,2),N=D[0],L=D[1];return Object(o.useEffect)((function(){O((null===t||void 0===t?void 0:t.filter((function(e){return e.archived})))||[]),L((null===t||void 0===t?void 0:t.filter((function(e){return!e.archived})))||[])}),[t]),Object(w.jsx)(l.a,{children:Object(w.jsxs)("section",{className:"Tags container",children:[Object(w.jsx)(p.a,{className:"Tags__tabsContainer",children:Object(w.jsxs)(y.a,{value:m,onChange:function(e,t){b(t),x.b(s.a.tags.tabChange)},"aria-label":"simple tabs example",indicatorColor:"primary",className:"Tags__tabsContainer__tabs",children:[Object(w.jsx)(C.a,{label:"Tags"}),Object(w.jsx)(C.a,{label:"Hidden Tags"})]})}),Object(w.jsx)(l.a,{children:Object(w.jsx)(I,{value:m,index:0,className:"Tags__tabPanel",children:Object(w.jsx)(_e,{tagsList:N,isTagsDataLoading:a,tagInfo:n,tagRuns:i,isRunsDataLoading:d,isTagInfoDataLoading:u})})}),Object(w.jsx)(l.a,{children:Object(w.jsx)(I,{value:m,index:1,className:"Tags__tabPanel",children:Object(w.jsx)(_e,{tagsList:h,isHiddenTagsList:!0,isTagsDataLoading:a,tagInfo:n,tagRuns:i,isRunsDataLoading:d,isTagInfoDataLoading:u})})}),(null===r||void 0===r?void 0:r.length)>0&&Object(w.jsx)(S.a,{handleClose:c,data:r})]})})}var Te=Object(o.memo)(xe),pe=_.getTagsData();t.default=function(){var e=Object(r.a)(_);return c.a.useEffect((function(){_.initialize(),pe.call(),x.a(s.a.tags.pageView)}),[]),Object(w.jsx)(l.a,{children:Object(w.jsx)(Te,{tagsListData:null===e||void 0===e?void 0:e.tagsList,isTagsDataLoading:null===e||void 0===e?void 0:e.isTagsDataLoading,tagInfo:null===e||void 0===e?void 0:e.tagInfo,tagRuns:null===e||void 0===e?void 0:e.tagRuns,onNotificationDelete:_.onNotificationDelete,notifyData:null===e||void 0===e?void 0:e.notifyData,isRunsDataLoading:null===e||void 0===e?void 0:e.isRunsDataLoading,isTagInfoDataLoading:null===e||void 0===e?void 0:e.isTagInfoDataLoading})})}},729:function(e,t,a){"use strict";a.d(t,"a",(function(){return s}));var n,i=a(0),o=["title","titleId"];function c(){return(c=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var a=arguments[t];for(var n in a)Object.prototype.hasOwnProperty.call(a,n)&&(e[n]=a[n])}return e}).apply(this,arguments)}function r(e,t){if(null==e)return{};var a,n,i=function(e,t){if(null==e)return{};var a,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||(i[a]=e[a]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(i[a]=e[a])}return i}function l(e,t){var a=e.title,l=e.titleId,s=r(e,o);return i.createElement("svg",c({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 44 44",ref:t,"aria-labelledby":l},s),a?i.createElement("title",{id:l},a):null,n||(n=i.createElement("path",{fill:"#30954c",d:"M22,3A19,19,0,1,0,41,22,19,19,0,0,0,22,3Zm8.53259,14.69269-9.8518,11.61108a1.50007,1.50007,0,0,1-2.2876,0l-4.9259-5.8056a1.5,1.5,0,1,1,2.28753-1.94086L19.537,26.01489l8.70813-10.26312a1.5,1.5,0,1,1,2.28747,1.94092Z"})))}var s=i.forwardRef(l);a.p},730:function(e,t,a){"use strict";a.d(t,"a",(function(){return s}));var n,i=a(0),o=["title","titleId"];function c(){return(c=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var a=arguments[t];for(var n in a)Object.prototype.hasOwnProperty.call(a,n)&&(e[n]=a[n])}return e}).apply(this,arguments)}function r(e,t){if(null==e)return{};var a,n,i=function(e,t){if(null==e)return{};var a,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||(i[a]=e[a]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(i[a]=e[a])}return i}function l(e,t){var a=e.title,l=e.titleId,s=r(e,o);return i.createElement("svg",c({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 44 44",ref:t,"aria-labelledby":l},s),a?i.createElement("title",{id:l},a):null,n||(n=i.createElement("path",{fill:"#cc231a",d:"M22,3A19,19,0,1,0,41,22,19,19,0,0,0,22,3Zm7.91309,24.794.1455.15332a1.50037,1.50037,0,0,1,.38477.48535,1.46959,1.46959,0,0,1,.1543.59863A1.49927,1.49927,0,0,1,29.6416,30.499a1.39236,1.39236,0,0,1-.61133.09864,1.48626,1.48626,0,0,1-.59961-.1543,1.551,1.551,0,0,1-.50976-.41309L22,24.11328l-5.94531,5.93555a1.49689,1.49689,0,0,1-.48584.38476,1.47552,1.47552,0,0,1-.59912.15528,1.33873,1.33873,0,0,1-.61084-.09864,1.505,1.505,0,0,1-.51953-.33886,1.474,1.474,0,0,1-.3379-.51856,1.49377,1.49377,0,0,1,.05616-1.21,1.55724,1.55724,0,0,1,.41211-.50976L19.605,22.27832l.28369-.28223-5.94678-5.94238a1.49988,1.49988,0,0,1,.41651-2.55225,1.441,1.441,0,0,1,.61133-.10009,1.4941,1.4941,0,0,1,.59912.15625,1.55409,1.55409,0,0,1,.51074.41211L22,19.88623l5.94434-5.94434a1.5084,1.5084,0,0,1,1.08593-.54052,1.43985,1.43985,0,0,1,.61133.10009,1.50239,1.50239,0,0,1,.80176,2.06641,1.57937,1.57937,0,0,1-.41309.51074l-5.91894,5.917Z"})))}var s=i.forwardRef(l);a.p},734:function(e,t,a){"use strict";var n=a(0),i=a.n(n),o=a(698),c=a(5),r=a(209),l=(a(737),a(1));function s(e){return Object(l.jsx)(r.a,{children:Object(l.jsxs)(o.a,{open:e.open,onClose:e.onCancel,"aria-labelledby":"dialog-title","aria-describedby":"dialog-description",PaperProps:{elevation:10},className:"ConfirmModal ConfirmModal__".concat(e.statusType),children:[Object(l.jsxs)("div",{className:"ConfirmModal__Body",children:[Object(l.jsx)(c.c,{size:"small",className:"ConfirmModal__Close__Icon",color:"secondary",withOnlyIcon:!0,onClick:e.onCancel,children:Object(l.jsx)(c.f,{name:"close"})}),Object(l.jsxs)("div",{className:"ConfirmModal__Title__Container",children:[Object(l.jsx)("div",{className:"ConfirmModal__Icon",children:e.icon}),e.title&&Object(l.jsx)(c.n,{size:16,tint:100,component:"h4",weight:600,children:e.title})]}),Object(l.jsxs)("div",{children:[e.description&&Object(l.jsx)(c.n,{className:"ConfirmModal__description",weight:400,component:"p",id:"dialog-description",children:e.description}),Object(l.jsxs)("div",{children:[e.text&&Object(l.jsx)(c.n,{className:"ConfirmModal__text",weight:400,component:"p",size:14,id:"dialog-description",children:e.text||""}),e.children&&e.children]})]})]}),Object(l.jsxs)("div",{className:"ConfirmModal__Footer",children:[Object(l.jsx)(c.c,{onClick:e.onCancel,className:"ConfirmModal__CancelButton",children:e.cancelBtnText}),Object(l.jsx)(c.c,{onClick:e.onSubmit,color:"primary",variant:"contained",className:"ConfirmModal__ConfirmButton",autoFocus:!0,children:e.confirmBtnText})]})]})})}s.defaultProps={confirmBtnText:"Confirm",cancelBtnText:"Cancel",statusType:"info"},s.displayName="ConfirmModal",t.a=i.a.memo(s)},737:function(e,t,a){},738:function(e,t,a){"use strict";a.d(t,"a",(function(){return u}));a(0);var n=a(69),i=a(1592),o=a(1595),c=a(711),r=a(729),l=a(730),s=a(12),d=(a(749),a(1));function u(e){var t=e.data,a=void 0===t?[]:t,u=e.handleClose;return Object(d.jsx)(s.a,{children:n.a.isEmpty(a)?null:Object(d.jsx)("div",{children:Object(d.jsx)(o.a,{open:!0,autoHideDuration:3e3,anchorOrigin:{vertical:"top",horizontal:"right"},children:Object(d.jsx)("div",{className:"NotificationContainer",children:a.map((function(e){var t=e.id,a=e.severity,n=e.messages;return Object(d.jsx)(c.a,{mt:.5,children:Object(d.jsx)(i.a,{onClose:function(){return u(+t)},variant:"outlined",severity:a,iconMapping:{success:Object(d.jsx)(r.a,{}),error:Object(d.jsx)(l.a,{})},style:{height:"auto"},children:Object(d.jsxs)("div",{className:"NotificationContainer__contentBox",children:[Object(d.jsx)("p",{className:"NotificationContainer__contentBox__severity",children:a}),n.map((function(e,t){return e?Object(d.jsx)("p",{className:"NotificationContainer__contentBox__message",children:e},t):null}))]})})},t)}))})})})})}},749:function(e,t,a){},859:function(e,t,a){}}]);
//# sourceMappingURL=tags.js.map?version=48027b75b97e020a2fcc