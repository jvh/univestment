(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{112:function(e,t,a){e.exports=a.p+"static/media/drawing.a80c8e89.svg"},113:function(e,t,a){},114:function(e,t,a){e.exports=a.p+"static/media/adzuna_logo.4b0be1b4.jpg"},134:function(e,t,a){e.exports=a.p+"static/media/marker.32d70ec7.png"},135:function(e,t,a){},136:function(e,t,a){e.exports=a.p+"static/media/logo_white.a794d802.svg"},137:function(e,t,a){"use strict";a.r(t);var n=a(0),l=a.n(n),o=a(38),r=a.n(o),c=(a(74),a(5)),i=a(6),s=a(9),m=a(7),u=a(8),p=a(16),d=(a(75),a(23)),E=a(13),h=(a(17),a(25)),f=a(21),g=a(140),v=a(63),b=a(61),y=a(62),N=a(138),O=a(64),_=a(139),w=a(141),k=a(58),S=a.n(k),C=a(20),j=a(27),x=a.n(j),z="http://api.univestment.co.uk",P=function(e){var t="where=".concat(e.where);return console.log("SEARCH PARAMS"),console.log(e),t=void 0===e.price_min?t:"".concat(t,"&price_min=").concat(e.price_min),t=void 0===e.price_max?t:"".concat(t,"&price_max=").concat(e.price_max),t=void 0===e.beds?t:"".concat(t,"&beds=").concat(e.beds),t=(t=(t=void 0===e.distance?t:"".concat(t,"&distance=").concat(e.distance)).replace(/,/gi,"")).replace(/ /gi,""),console.log(t),t},A={search:function(e){var t="".concat(z,"/search?").concat(P(e));return new Promise(function(e,a){x.a.get(t).then(function(t){e(t.data)}).catch(a)})},coords:function(e){var t="".concat(z,"/coords?").concat(P(e));return new Promise(function(e,a){x.a.get(t).then(function(t){e(t.data)}).catch(a)})}},F=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(s.a)(this,Object(m.a)(t).call(this,e))).advOptions=function(){a.setState({isOpened:!a.state.isOpened}),null!==a.props.collapse&&a.props.collapse()},a.validatePostcode=function(e){e=e.replace(/\s/g,"");var t=/^[A-Z]{1,2}[0-9]{1,2}[A-Z]{0,1} ?[0-9][A-Z]{2}$/i;return console.log(t.test(e)),t.test(e)},a.handleSwitchChange=function(){a.setState({uniSearch:!a.state.uniSearch})},a.handleFormChange=function(e){console.log("CHANGE");var t=e.target.value,n=e.target.name;if(console.log(n+" > "+t),"where"===n){var l=a.validatePostcode(t);console.log(l),a.setState({isSubmitEnabled:l})}a.setState({form:Object(f.a)({},a.state.form,Object(h.a)({},n,t))})},a.state={form:{where:""},isOpened:e.isOpened,isSubmitEnabled:!1,uniSearch:!1},a.handleFormChange=a.handleFormChange.bind(Object(E.a)(a)),a}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return l.a.createElement("div",null,l.a.createElement(g.a,{onSubmit:this.handleSubmit},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Location"),l.a.createElement(b.a,{controlId:"postcode"},l.a.createElement(y.a,{name:"where",type:"text",value:this.state.form.where,placeholder:"Please enter Postcode...",onChange:this.handleFormChange})),l.a.createElement(N.a,null,l.a.createElement(b.a,{as:O.a,controlId:"min_price"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Min Price"),l.a.createElement(_.a,null,l.a.createElement(_.a.Prepend,null,l.a.createElement(_.a.Text,{id:"inputGroupPrepend"},"\xa3")),l.a.createElement(y.a,{as:"select",name:"price_min",value:this.state.form.price_min,onChange:this.handleFormChange},l.a.createElement("option",null,"No min"),l.a.createElement("option",null,"10,000"),l.a.createElement("option",null,"20,000"),l.a.createElement("option",null,"30,000"),l.a.createElement("option",null,"40,000"),l.a.createElement("option",null,"50,000"),l.a.createElement("option",null,"60,000"),l.a.createElement("option",null,"70,000"),l.a.createElement("option",null,"80,000"),l.a.createElement("option",null,"90,000"),l.a.createElement("option",null,"100,000"),l.a.createElement("option",null,"110,000"),l.a.createElement("option",null,"120,000"),l.a.createElement("option",null,"130,000"),l.a.createElement("option",null,"140,000"),l.a.createElement("option",null,"150,000"),l.a.createElement("option",null,"175,000"),l.a.createElement("option",null,"200,000"),l.a.createElement("option",null,"225,000"),l.a.createElement("option",null,"250,000"),l.a.createElement("option",null,"275,000"),l.a.createElement("option",null,"300,000"),l.a.createElement("option",null,"325,000"),l.a.createElement("option",null,"350,000"),l.a.createElement("option",null,"375,000"),l.a.createElement("option",null,"400,000"),l.a.createElement("option",null,"450,000"),l.a.createElement("option",null,"500,000"),l.a.createElement("option",null,"550,000"),l.a.createElement("option",null,"600,000"),l.a.createElement("option",null,"650,000"),l.a.createElement("option",null,"700,000"),l.a.createElement("option",null,"800,000"),l.a.createElement("option",null,"900,000"),l.a.createElement("option",null,"1,000,000"),l.a.createElement("option",null,"1,100,000"),l.a.createElement("option",null,"1,200,000"),l.a.createElement("option",null,"1,300,000"),l.a.createElement("option",null,"1,400,000"),l.a.createElement("option",null,"1,500,000"),l.a.createElement("option",null,"1,750,000"),l.a.createElement("option",null,"2,000,000")))),l.a.createElement(b.a,{as:O.a,controlId:"min_price"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Max Price"),l.a.createElement(_.a,null,l.a.createElement(_.a.Prepend,null,l.a.createElement(_.a.Text,{id:"inputGroupPrepend"},"\xa3")),l.a.createElement(y.a,{as:"select",name:"price_max",value:this.state.form.price_max,onChange:this.handleFormChange},l.a.createElement("option",null,"No max"),l.a.createElement("option",null,"10,000"),l.a.createElement("option",null,"20,000"),l.a.createElement("option",null,"30,000"),l.a.createElement("option",null,"40,000"),l.a.createElement("option",null,"50,000"),l.a.createElement("option",null,"60,000"),l.a.createElement("option",null,"70,000"),l.a.createElement("option",null,"80,000"),l.a.createElement("option",null,"90,000"),l.a.createElement("option",null,"100,000"),l.a.createElement("option",null,"110,000"),l.a.createElement("option",null,"120,000"),l.a.createElement("option",null,"130,000"),l.a.createElement("option",null,"140,000"),l.a.createElement("option",null,"150,000"),l.a.createElement("option",null,"175,000"),l.a.createElement("option",null,"200,000"),l.a.createElement("option",null,"225,000"),l.a.createElement("option",null,"250,000"),l.a.createElement("option",null,"275,000"),l.a.createElement("option",null,"300,000"),l.a.createElement("option",null,"325,000"),l.a.createElement("option",null,"350,000"),l.a.createElement("option",null,"375,000"),l.a.createElement("option",null,"400,000"),l.a.createElement("option",null,"450,000"),l.a.createElement("option",null,"500,000"),l.a.createElement("option",null,"550,000"),l.a.createElement("option",null,"600,000"),l.a.createElement("option",null,"650,000"),l.a.createElement("option",null,"700,000"),l.a.createElement("option",null,"800,000"),l.a.createElement("option",null,"900,000"),l.a.createElement("option",null,"1,000,000"),l.a.createElement("option",null,"1,100,000"),l.a.createElement("option",null,"1,200,000"),l.a.createElement("option",null,"1,300,000"),l.a.createElement("option",null,"1,400,000"),l.a.createElement("option",null,"1,500,000"),l.a.createElement("option",null,"1,750,000"),l.a.createElement("option",null,"\xa32,000,000")))),l.a.createElement(b.a,{as:O.a,controlId:"min_price"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Min. Beds"),l.a.createElement(y.a,{as:"select",name:"beds",value:this.state.form.beds,onChange:this.handleFormChange},l.a.createElement("option",null,"No min"),l.a.createElement("option",null,"1"),l.a.createElement("option",null,"2"),l.a.createElement("option",null,"3"),l.a.createElement("option",null,"4"),l.a.createElement("option",null,"5"),l.a.createElement("option",null,"6"),l.a.createElement("option",null,"7"),l.a.createElement("option",null,"8"),l.a.createElement("option",null,"9"),l.a.createElement("option",null,"10")))),l.a.createElement(C.Collapse,{isOpened:this.state.isOpened,hasNestedCollapse:!0},l.a.createElement(N.a,null,l.a.createElement(b.a,{as:O.a,controlId:"distance"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Distance from Location"),l.a.createElement(_.a,null,l.a.createElement(y.a,{as:"select",name:"distance",value:this.state.form.distance,onChange:this.handleFormChange},l.a.createElement("option",null,"1"),l.a.createElement("option",null,"2"),l.a.createElement("option",null,"3"),l.a.createElement("option",null,"5"),l.a.createElement("option",null,"10"),l.a.createElement("option",null,"15"),l.a.createElement("option",null,"20"),l.a.createElement("option",null,"30"),l.a.createElement("option",null,"40")),l.a.createElement(_.a.Append,null,l.a.createElement(_.a.Text,{id:"inputGroupAppend"},"km")))),l.a.createElement(b.a,{as:O.a,controlId:"property_type"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Property Type"),l.a.createElement(y.a,{as:"select",name:"property_type",value:this.state.form.prop_type,onChange:this.handleFormChange},l.a.createElement("option",null,"Show All"),l.a.createElement("option",null,"Houses"),l.a.createElement("option",null,"Flats")))),l.a.createElement(N.a,null,l.a.createElement(b.a,{as:O.a,className:"col-4",controlId:"university_search"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"University Search?"),l.a.createElement("div",{className:"switch-pad"},l.a.createElement("div",{className:"switch-inner"},l.a.createElement(S.a,{onChange:this.handleSwitchChange,checked:this.state.uniSearch,className:"react-switch"})))),l.a.createElement(b.a,{as:O.a,className:"col-8",controlId:"university_search"},l.a.createElement(C.Collapse,{isOpened:this.state.uniSearch},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Distance From University"),l.a.createElement(y.a,{as:"select",name:"km_away_from_uni",value:this.state.form.km_away_from_uni,onChange:this.handleFormChange},l.a.createElement("option",null,"1"),l.a.createElement("option",null,"2"),l.a.createElement("option",null,"3"),l.a.createElement("option",null,"4"),l.a.createElement("option",null,"5")))))),l.a.createElement(N.a,{className:"pad-top"},l.a.createElement(b.a,{as:O.a,controlId:"advanced"},l.a.createElement("div",{className:"text-left"},l.a.createElement(w.a,{variant:"link",onClick:this.advOptions},"Advanced Options..."))),l.a.createElement(b.a,{as:O.a,controlId:"search"},l.a.createElement("div",{className:"text-right"},l.a.createElement(p.b,{to:{pathname:"/search",state:{form:this.state.form}}},l.a.createElement(w.a,{type:"button",disabled:!this.state.isSubmitEnabled},"Search")))))))}}]),t}(n.Component),I=(a(22),function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(s.a)(this,Object(m.a)(t).call(this,e))).state={isOpened:!1},a.collapse=a.collapse.bind(Object(E.a)(a)),a}return Object(u.a)(t,e),Object(i.a)(t,[{key:"collapse",value:function(){this.setState({isOpened:!this.state.isOpened})}},{key:"render",value:function(){return l.a.createElement("div",null,l.a.createElement("div",{className:"homebackground"},l.a.createElement("div",{className:"grad"},l.a.createElement("div",{className:"background-content"},l.a.createElement(C.Collapse,{isOpened:!this.state.isOpened},l.a.createElement("div",{className:"logo-container"},l.a.createElement("img",{className:"title-logo",src:a(112)})),l.a.createElement("div",{className:"homeTitle container align-center"},l.a.createElement("h1",{className:"title"},"PropertyMonopoly"))),l.a.createElement("div",{className:"centre"},l.a.createElement("div",{className:"homeDiv"},l.a.createElement("div",{className:"transparent container-xsmall more-rounded"},l.a.createElement(F,Object.assign({collapse:this.collapse,isOpened:this.state.isOpened},this.props)))))))))}}]),t}(n.Component)),D=a(68),L=a(11),T="#09274d",M=function(e){function t(){return Object(c.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"componentDidMount",value:function(){this.drawChart()}},{key:"drawChart",value:function(){var e=this.props.data,t=this.props.height,a=this.props.width,n=Math.max.apply(Math,Object(D.a)(e));console.log(n);var l=t/(n+n/10);L.h("body").append("svg").attr("width",a).attr("height",t).style("margin-left",100).selectAll("rect").data(e).enter().append("rect").attr("x",function(e,t){return 70*t}).attr("y",function(e,t){return 500-l*e}).attr("width",65).attr("height",function(e,t){return e*l}).attr("fill",T)}},{key:"render",value:function(){return l.a.createElement("div",{id:"#"+this.props.id})}}]),t}(n.Component),W=[12,5,6,6,9,10,15,5,3],R=[{property:{adzuna:{__CLASS__:"Adzuna::API::Response::Property",adref:"eyJhbGciOiJIUzI1NiJ9.eyJpIjoxMTE0ODQ2NzYxLCJzIjoiTDM2aWZzcHpULWU4QXRJVkpUN2ZIQSJ9.aSOZYQoAZoantJMeCJLmEm26mDl1IzVZufFSZlcE0Nw",beds:1,category:{__CLASS__:"Adzuna::API::Response::Category",label:"For Sale",tag:"for-sale"},created:"2019-03-29T14:13:56Z",description:"This superb one bedroom ground floor apartment is situated in the sought after area of Millbrook and is offered with no forward chain. This is an ideal investment opportunity and could also be suited to first time buyers. The property benefits from having underfloor heating.",id:1114846761,image_url:"https://s3-eu-west-1.amazonaws.com/property.adzuna.co.uk/a59e47e1c5ddd2fdfd53dd426f9f2169a471092ec1f0eaab81bc08c985e5f61f.jpeg",is_furnished:"0",latitude:50.928699,location:{__CLASS__:"Adzuna::API::Response::Location",area:["UK","South East England","Hampshire","Southampton"],display_name:"Southampton, Hampshire"},longitude:-1.44911,postcode:"SO164PU",property_type:"flat",redirect_url:"https://property.adzuna.co.uk/land/ad/1114846761?se=L36ifspzT-e8AtIVJT7fHA&utm_medium=api&utm_source=d1b12649&v=65068C80F9B11360879A34F9D8046DF278E1CBFF",sale_price:1e5,title:"1 bed flat for sale in Wimpson Lane"},investment_type:"flip",market_value:13e4},historic_data:{outcode:{historic:{x:[0,1,3,4,5,7,8,9,10],y:[13,24,46,68,89,102,114]},predicted:{x:[11,12,13,14,15,17,19],y:[123,124,146,168,189,202,214]}}}}],G=function(e){function t(){var e;return Object(c.a)(this,t),(e=Object(s.a)(this,Object(m.a)(t).call(this))).isLoading=function(){return null===e.state.data&&!e.hasError()},e.hasError=function(){return null!==e.state.error},e.handleGetDataSuccess=function(t){console.log(t),e.setState({data:t.result.data}),console.log(e.state)},e.handleGetDataFailure=function(e){console.log(e)},e.fetchData=function(){A.getData().then(e.handleGetDataSuccess).catch(e.handleGetDataFailure)},e.state={data:null,error:null},e}return Object(u.a)(t,e),Object(i.a)(t,[{key:"componentDidMount",value:function(){this.fetchData()}},{key:"getBarGraph",value:function(e){}},{key:"render",value:function(){return this.isLoading()?l.a.createElement("div",null):this.hasError()?l.a.createElement("div",null):l.a.createElement("div",{className:"App"},l.a.createElement("h1",null,"Bar Chart"),l.a.createElement(M,{data:this.state.data,height:"500",width:"700"}))}}]),t}(n.Component),U=(a(113),function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(s.a)(this,Object(m.a)(t).call(this,e))).state={historic:e.data.historic,predicted:e.data.predicted},a}return Object(u.a)(t,e),Object(i.a)(t,[{key:"componentDidMount",value:function(){console.log("SERIES"),console.log(this.props),this.drawChart()}},{key:"drawChart",value:function(){var e=[{label:"historic",x:this.state.historic.x,y:this.state.historic.y},{label:"predicted",x:this.state.predicted.x,y:this.state.predicted.y}],t=this.node,a=50,n=50,l=50,o=50,r=this.props.width-o-n,c=this.props.height-a-l,i=L.g().range([0,r]).domain([L.f(e,function(e){return L.f(e.x)}),L.e(e,function(e){return L.e(e.x)})]),s=L.g().range([c,0]).domain([L.f(e,function(e){return L.f(e.y)}),L.e(e,function(e){return L.e(e.y)})]),m=L.d().x(function(e,t){return i(e[0])}).y(function(e){return s(e[1])}).curve(L.c),u=L.h(t).append("svg").attr("width",r+o+n).attr("height",c+a+l).attr("style","display:block").append("g").attr("transform","translate("+o+","+a+")");u.append("g").attr("class","x axis").attr("transform","translate(0,"+c+")").call(L.a(i)),u.append("g").attr("class","y axis").call(L.b(s)),u.selectAll(".d3_xy_chart_line").data(e.map(function(e){return L.i(e.x,e.y)})).enter().append("g").attr("class","d3_xy_chart_line").append("path").attr("class","line").attr("d",function(e){return m(e)}).attr("stroke","black"),u.append("path").datum(e).attr("class","line").attr("d",m)}},{key:"render",value:function(){var e=this;return l.a.createElement("svg",{className:"graph",ref:function(t){return e.node=t},width:this.props.width,height:this.props.height})}}]),t}(n.Component)),J=function(e){return l.a.createElement("div",{className:"App"},l.a.createElement("h1",null,"Line Graph"),l.a.createElement(U,{data:W}))},B=function(e){console.log("CARD PROPS"),console.log(e);var t=e.property.adzuna,n=(e.all_results,t.image_url),o=t.description;if(o.length>150){var r=(o=o.substr(0,150)).lastIndexOf(" ");o=o.substr(0,r)+" ..."}return console.log(n),l.a.createElement("div",null,l.a.createElement("div",{className:"spacer-sml"}),l.a.createElement("div",{className:"row result results-bg rounded"},l.a.createElement("div",{className:"col-sm-12 col-md-4"},l.a.createElement("div",{className:"result-card"},l.a.createElement(p.b,{to:{pathname:"/property",state:{form:e}}},l.a.createElement("img",{className:"result-image",src:n,alt:""})))),l.a.createElement("div",{className:"col-sm-12 col-md-8"},l.a.createElement("div",{className:"row pad-top"},l.a.createElement("div",{className:"col-9"},l.a.createElement("h3",{className:"align-left"},t.title),l.a.createElement("p",{style:{fontSize:"125%"},className:"align-left"},t.location.display_name)),l.a.createElement("div",{className:"col-3"},l.a.createElement("h3",{className:"align-right"},"\xa3",t.sale_price),l.a.createElement("p",{className:"align-right"},"guide price")),l.a.createElement("div",{className:"col-12 description",style:{display:"inline-block"}},l.a.createElement("p",{style:{fontSize:"85%"}},o,l.a.createElement(p.b,{to:{pathname:"/property",state:{form:e}}},l.a.createElement("a",{href:t.redirect_url,target:"_blank",rel:"noopener noreferrer"}," (Read more...)"))))),l.a.createElement("div",{className:"row"},l.a.createElement("div",{className:"align-right adzuna-text pad-hor",style:{whiteSpace:"nowrap"}},l.a.createElement("a",{href:t.redirect_url,target:"_blank",rel:"noopener noreferrer",style:{position:"relative",top:"2px"}},"Properties by "),l.a.createElement("a",{href:t.redirect_url,target:"_blank",rel:"noopener noreferrer"},l.a.createElement("img",{className:"adzuna_logo",src:a(114),alt:""})))),l.a.createElement("div",null))))},H=function(e){var t=Array.from(e.search.search_results);return console.log(t),t&&t.length>0?l.a.createElement("div",{className:"container-small"},t.map(function(t){return l.a.createElement(B,Object.assign({},t,{search:e.search}))}),l.a.createElement("div",{className:"spacer-sml"})):null},Z=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(s.a)(this,Object(m.a)(t).call(this,e))).advOptions=function(){a.setState({isOpened:!a.state.isOpened}),console.log(a.state.isOpened)},a.handleFormChange=function(e){var t=e.target.value,n=e.target.name;a.setState({form:Object(f.a)({},a.state.form,Object(h.a)({},n,t))})},a.state={form:{location:""},isOpened:!1},a.handleFormChange=a.handleFormChange.bind(Object(E.a)(a)),a}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return l.a.createElement("div",null,l.a.createElement(g.a,{onSubmit:this.handleSubmit},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Location"),l.a.createElement(b.a,{controlId:"postcode"},l.a.createElement(y.a,{name:"location",type:"text",value:this.state.form.location,placeholder:"Please enter Postcode...",onChange:this.handleFormChange})),l.a.createElement(N.a,null,l.a.createElement(b.a,{as:O.a,controlId:"min_price"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Min Price"),l.a.createElement(_.a,null,l.a.createElement(_.a.Prepend,null,l.a.createElement(_.a.Text,{id:"inputGroupPrepend"},"\xa3")),l.a.createElement(y.a,{as:"select",name:"min_price",value:this.state.form.min_price,onChange:this.handleFormChange},l.a.createElement("option",null,"No min"),l.a.createElement("option",null,"10,000"),l.a.createElement("option",null,"20,000"),l.a.createElement("option",null,"30,000"),l.a.createElement("option",null,"40,000"),l.a.createElement("option",null,"50,000"),l.a.createElement("option",null,"60,000"),l.a.createElement("option",null,"70,000"),l.a.createElement("option",null,"80,000"),l.a.createElement("option",null,"90,000"),l.a.createElement("option",null,"100,000"),l.a.createElement("option",null,"110,000"),l.a.createElement("option",null,"120,000"),l.a.createElement("option",null,"130,000"),l.a.createElement("option",null,"140,000"),l.a.createElement("option",null,"150,000"),l.a.createElement("option",null,"175,000"),l.a.createElement("option",null,"200,000"),l.a.createElement("option",null,"225,000"),l.a.createElement("option",null,"250,000"),l.a.createElement("option",null,"275,000"),l.a.createElement("option",null,"300,000"),l.a.createElement("option",null,"325,000"),l.a.createElement("option",null,"350,000"),l.a.createElement("option",null,"375,000"),l.a.createElement("option",null,"400,000"),l.a.createElement("option",null,"450,000"),l.a.createElement("option",null,"500,000"),l.a.createElement("option",null,"550,000"),l.a.createElement("option",null,"600,000"),l.a.createElement("option",null,"650,000"),l.a.createElement("option",null,"700,000"),l.a.createElement("option",null,"800,000"),l.a.createElement("option",null,"900,000"),l.a.createElement("option",null,"1,000,000"),l.a.createElement("option",null,"1,100,000"),l.a.createElement("option",null,"1,200,000"),l.a.createElement("option",null,"1,300,000"),l.a.createElement("option",null,"1,400,000"),l.a.createElement("option",null,"1,500,000"),l.a.createElement("option",null,"1,750,000"),l.a.createElement("option",null,"2,000,000")))),l.a.createElement(b.a,{as:O.a,controlId:"min_price"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Max Price"),l.a.createElement(_.a,null,l.a.createElement(_.a.Prepend,null,l.a.createElement(_.a.Text,{id:"inputGroupPrepend"},"\xa3")),l.a.createElement(y.a,{as:"select",name:"max_price",value:this.state.form.max_price,onChange:this.handleFormChange},l.a.createElement("option",null,"No max"),l.a.createElement("option",null,"10,000"),l.a.createElement("option",null,"20,000"),l.a.createElement("option",null,"30,000"),l.a.createElement("option",null,"40,000"),l.a.createElement("option",null,"50,000"),l.a.createElement("option",null,"60,000"),l.a.createElement("option",null,"70,000"),l.a.createElement("option",null,"80,000"),l.a.createElement("option",null,"90,000"),l.a.createElement("option",null,"100,000"),l.a.createElement("option",null,"110,000"),l.a.createElement("option",null,"120,000"),l.a.createElement("option",null,"130,000"),l.a.createElement("option",null,"140,000"),l.a.createElement("option",null,"150,000"),l.a.createElement("option",null,"175,000"),l.a.createElement("option",null,"200,000"),l.a.createElement("option",null,"225,000"),l.a.createElement("option",null,"250,000"),l.a.createElement("option",null,"275,000"),l.a.createElement("option",null,"300,000"),l.a.createElement("option",null,"325,000"),l.a.createElement("option",null,"350,000"),l.a.createElement("option",null,"375,000"),l.a.createElement("option",null,"400,000"),l.a.createElement("option",null,"450,000"),l.a.createElement("option",null,"500,000"),l.a.createElement("option",null,"550,000"),l.a.createElement("option",null,"600,000"),l.a.createElement("option",null,"650,000"),l.a.createElement("option",null,"700,000"),l.a.createElement("option",null,"800,000"),l.a.createElement("option",null,"900,000"),l.a.createElement("option",null,"1,000,000"),l.a.createElement("option",null,"1,100,000"),l.a.createElement("option",null,"1,200,000"),l.a.createElement("option",null,"1,300,000"),l.a.createElement("option",null,"1,400,000"),l.a.createElement("option",null,"1,500,000"),l.a.createElement("option",null,"1,750,000"),l.a.createElement("option",null,"\xa32,000,000")))),l.a.createElement(b.a,{as:O.a,controlId:"min_price"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Min. Beds"),l.a.createElement(y.a,{as:"select",name:"min_beds",value:this.state.form.min_beds,onChange:this.handleFormChange},l.a.createElement("option",null,"No min"),l.a.createElement("option",null,"1"),l.a.createElement("option",null,"2"),l.a.createElement("option",null,"3"),l.a.createElement("option",null,"4"),l.a.createElement("option",null,"5"),l.a.createElement("option",null,"6"),l.a.createElement("option",null,"7"),l.a.createElement("option",null,"8"),l.a.createElement("option",null,"9"),l.a.createElement("option",null,"10")))),l.a.createElement(N.a,null,l.a.createElement(C.Collapse,{isOpened:this.state.isOpened},l.a.createElement(b.a,{as:O.a,controlId:"distance"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Distance from Location"),l.a.createElement(_.a,null,l.a.createElement(y.a,{as:"select"},'name="distance" value=',this.state.form.distance,"defaultValue=10 onChange=",this.handleFormChange,">",l.a.createElement("option",null,"1"),l.a.createElement("option",null,"2"),l.a.createElement("option",null,"3"),l.a.createElement("option",null,"5"),l.a.createElement("option",null,"10"),l.a.createElement("option",null,"15"),l.a.createElement("option",null,"20"),l.a.createElement("option",null,"30"),l.a.createElement("option",null,"40")),l.a.createElement(_.a.Append,null,l.a.createElement(_.a.Text,{id:"inputGroupAppend"},"km")))),l.a.createElement(b.a,{as:O.a,controlId:"property_type"},l.a.createElement(v.a,{style:{fontWeight:"bold"}},"Property Type"),l.a.createElement(y.a,{as:"select"},'name="property_type" value=',this.state.form.prop_type,"onChange=",this.handleFormChange,">",l.a.createElement("option",null,"Show All"),l.a.createElement("option",null,"Houses"),l.a.createElement("option",null,"Flats"))))),l.a.createElement(N.a,{className:"pad-top"},l.a.createElement(b.a,{as:O.a,controlId:"advanced"},l.a.createElement("div",{className:"text-left"},l.a.createElement(w.a,{variant:"link",onClick:this.advOptions},"Advanced Options..."))),l.a.createElement(b.a,{as:O.a,controlId:"search"},l.a.createElement("div",{className:"text-right"},l.a.createElement(p.b,{to:{pathname:"/search",state:{form:this.state.form}}},l.a.createElement(w.a,{type:"button"},"Search")))))))}}]),t}(n.Component),V=a(67),Q=a.n(V),Y=function(){return l.a.createElement("div",null,l.a.createElement("img",{className:"marker",style:{cursor:"pointer"},src:a(134)}))},K=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(s.a)(this,Object(m.a)(t).call(this,e))).handleCoordSuccess=function(e){console.log("COORDS"),console.log(e),a.setState({center:{lng:e[0],lat:e[1]},isLoading:!1})},a.handleCoordsFailure=function(e){console.log("FAIL")},a.state={results:e.results,zoom:11,isLoading:!0},a}return Object(u.a)(t,e),Object(i.a)(t,[{key:"componentDidMount",value:function(){console.log(this.props.where);var e={where:this.props.where};A.coords(e).then(this.handleCoordSuccess).catch(this.handleCoordsFailure)}},{key:"placePins",value:function(){return this.state.results.map(function(e,t){return console.log("RESULT"),console.log(e),null==e.property.adzuna.latitude||null==e.property.adzuna.longitude?null:l.a.createElement(Y,{lat:e.property.adzuna.latitude,lng:e.property.adzuna.longitude})})}},{key:"render",value:function(){return this.state.isLoading?l.a.createElement("div",null):l.a.createElement("div",{className:"map rounded"},l.a.createElement(Q.a,{bootstrapURLKeys:{key:"AIzaSyCElo3BDmiGTGaF6E-Cq6aVwgiihfPPA7c"},defaultCenter:this.state.center,defaultZoom:this.state.zoom},this.placePins()))}}]),t}(n.Component);K.defaultProps={center:{lat:50.934502,lng:-1.45786},zoom:11};var $=K,q=(a(135),function(){return l.a.createElement("div",{className:"loading"},l.a.createElement("div",{className:"sk-cube-grid"},l.a.createElement("div",{className:"sk-cube sk-cube1"}),l.a.createElement("div",{className:"sk-cube sk-cube2"}),l.a.createElement("div",{className:"sk-cube sk-cube3"}),l.a.createElement("div",{className:"sk-cube sk-cube4"}),l.a.createElement("div",{className:"sk-cube sk-cube5"}),l.a.createElement("div",{className:"sk-cube sk-cube6"}),l.a.createElement("div",{className:"sk-cube sk-cube7"}),l.a.createElement("div",{className:"sk-cube sk-cube8"}),l.a.createElement("div",{className:"sk-cube sk-cube9"})),l.a.createElement("div",null,l.a.createElement("h3",{className:"align-center pad-top"},"Crunching the Numbers...")))}),X=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(s.a)(this,Object(m.a)(t).call(this,e))).handleSearchSuccess=function(e){console.log(e),console.log(R),a.setState({search:{form:a.state.form,search_results:e}}),console.log(),a.setState({isLoading:!1})},a.handleSearchFailure=function(e){},a.state={width:0,height:0,isLoading:!0},a.updateWindowDimensions=a.updateWindowDimensions.bind(Object(E.a)(a)),a}return Object(u.a)(t,e),Object(i.a)(t,[{key:"componentWillUnmount",value:function(){window.removeEventListener("resize",this.updateWindowDimensions)}},{key:"updateWindowDimensions",value:function(){this.setState({width:window.innerWidth,height:window.innerHeight})}},{key:"componentDidMount",value:function(){this.setState({isLoading:!0}),console.log("RESULTS"),console.log(this.props.location.state),console.log(this.props.location.state.search),this.updateWindowDimensions(),window.addEventListener("resize",this.updateWindowDimensions),void 0===this.props.location.state&&(window.location="/"),void 0===this.props.location.state.search||null===this.props.location.state.search?(console.log("HANDLE SUBMIT"),this.handleSubmit()):(console.log("SET STATE"),console.log(this.props.location.state.search.form),this.setState({search:this.props.location.state.search,isLoading:!1,form:this.props.location.state.search.form}))}},{key:"handleSubmit",value:function(){console.log("Submit");var e=this.props.location.state.form,t=e.where,a=e.price_min,n=e.price_max,l=e.beds,o=e.distance;e.uni_search,e.km_away_from_uni;this.setState({form:this.props.location.state.form});var r={where:t};r="No min"===a||void 0===a?r:Object(f.a)({},r,{price_min:a}),r="No max"===n||void 0===n?r:Object(f.a)({},r,{price_max:n}),r="No min"===l||void 0===l?r:Object(f.a)({},r,{beds:l}),r=void 0===o?r:Object(f.a)({},r,{distance:o}),console.log("search"),A.search(r).then(this.handleSearchSuccess).catch(this.handleSearchFailure)}},{key:"render",value:function(){return this.state.isLoading?l.a.createElement(q,null):this.state.width<1830?l.a.createElement("div",null,l.a.createElement("div",{className:"container-small"},l.a.createElement("div",{className:"spacer-sml"}),l.a.createElement("div",{className:"row-pad row result rounded results-bg"},l.a.createElement("div",{className:"col-12"},l.a.createElement(Z,this.props)))),l.a.createElement("div",{className:"container-small"},l.a.createElement("div",{className:"spacer-sml"}),l.a.createElement("div",{className:"row result results-bg"},l.a.createElement($,{results:this.state.search.search_results,where:this.state.form.where}))),l.a.createElement(H,{search:this.state.search})):l.a.createElement("div",{className:"container-large"},l.a.createElement("div",{className:"row"},l.a.createElement("div",{className:"col-6"},l.a.createElement(H,{search:this.state.search,s:!0})),l.a.createElement("div",{className:"col-6"},l.a.createElement("div",{className:"container-small"},l.a.createElement("div",{className:"spacer-sml"}),l.a.createElement("div",{className:"row-pad row result rounded results-bg"},l.a.createElement("div",{className:"col-12"},l.a.createElement(Z,this.props)))),l.a.createElement("div",{className:"container-small"},l.a.createElement("div",{className:"spacer-sml"}),l.a.createElement("div",{className:"row result results-bg"},l.a.createElement($,{results:this.state.search.search_results,where:this.state.form.where})),l.a.createElement("div",{className:"spacer-sml"})))))}}]),t}(n.Component),ee=function(e){function t(e){var a;return Object(c.a)(this,t),a=Object(s.a)(this,Object(m.a)(t).call(this,e)),void 0===e.location.state&&(window.location="/"),a.state={data:e.location.state.form,adzuna:e.location.state.form.property.adzuna,search:e.location.state.form.search},console.log("PROPERTY PROPS"),console.log(e),a}return Object(u.a)(t,e),Object(i.a)(t,[{key:"componentDidMount",value:function(){console.log("HISTORIC"),console.log(this.state.data)}},{key:"back",value:function(){}},{key:"render",value:function(){return l.a.createElement("div",{className:"bg outer pad-top pad-bottom"},l.a.createElement("div",{className:"results-bg container-small"},l.a.createElement("div",{className:"row-pad"},l.a.createElement("div",null,l.a.createElement(p.b,{to:{pathname:"/search",state:{search:this.state.search}}},l.a.createElement("a",{style:{cursor:"pointer"},onClick:this.back},"<< Back to Search Results")),l.a.createElement("br",null),l.a.createElement("div",{className:"row pad-top"},l.a.createElement("div",{className:"col-10"},l.a.createElement("h1",{className:"align-left"},this.state.adzuna.title),l.a.createElement("p",{style:{fontSize:"125%"},className:"align-left"},this.state.adzuna.location.display_name)),l.a.createElement("div",{className:"col-2"},l.a.createElement("h3",{className:"align-right"},"\xa3",this.state.adzuna.sale_price),l.a.createElement("p",{className:"align-right"},"guide price"))))),l.a.createElement("div",null,l.a.createElement("a",{href:this.state.adzuna.redirect_url,target:"_blank",rel:"noopener noreferrer"},l.a.createElement("img",{className:"property-image",src:this.state.adzuna.image_url,alt:""}))),l.a.createElement("div",{className:"row row-pad"},l.a.createElement("div",{className:"description"},l.a.createElement("p",null,this.state.adzuna.description),l.a.createElement("a",{href:this.state.adzuna.redirect_url,target:"_blank",rel:"noopener noreferrer",style:{float:"right",display:"inline"}},"Read More..."))),l.a.createElement("div",{className:"pad-hor-both pad-top"},l.a.createElement("div",{className:"overline pad-top"},l.a.createElement("div",null,l.a.createElement("h1",{className:"align-center value-green",style:{fontSize:"350%"}},"\xa3",this.state.data.property.investment.market_value-this.state.adzuna.sale_price),l.a.createElement("h3",{className:"align-center"},"Below Estimated Market Value")))),l.a.createElement("div",{className:"pad-hor-both",style:{textAlign:"justify"}},l.a.createElement("p",{className:"align-center"}," The market value for this area has been estimated at \xa3",this.state.data.property.market_value," meaning that this property has a potential return of investment of up to \xa3",this.state.data.property.market_value-this.state.adzuna.sale_price)),l.a.createElement("div",{className:"pad-hor-both pad-top"},l.a.createElement("div",null,l.a.createElement("h1",{className:"align-center value-green",style:{fontSize:"350%"}},"\xa3650 PCM"),l.a.createElement("h3",{className:"align-center"},"Average Rental in Local Area"))),l.a.createElement("div",{className:"pad-hor-both",style:{textAlign:"justify"}},l.a.createElement("p",{className:"align-center"}," The market value for this area has been estimated at \xa3",this.state.data.property.market_value," meaning that this property has a potential return of investment of up to \xa3",this.state.data.property.market_value-this.state.adzuna.sale_price)),l.a.createElement("div",{className:"pad-hor-both pad-top"},l.a.createElement("div",{className:"graph-outer overline pad-top"},l.a.createElement("h1",{className:"align-center",style:{fontSize:"275%"}},"Market Value Prediction"),l.a.createElement(U,{width:"700",height:"500",data:this.state.data.historic_data.outcode})))))}}]),t}(n.Component),te=function(e){var t=function(e){return function(t){return function(a){return l.a.createElement(e,Object.assign({},a,t))}}},a=t(I)(e),n=t(G)(e),o=(t(J)(e),t(X)(e)),r=t(ee)(e);return l.a.createElement("main",null,l.a.createElement(d.c,null,l.a.createElement(d.a,{exact:!0,path:"/",render:a}),l.a.createElement(d.a,{exact:!0,path:"/property",render:r}),l.a.createElement(d.a,{exact:!0,path:"/bar",render:n}),l.a.createElement(d.a,{exact:!0,path:"/search",render:o}),l.a.createElement(d.a,{exact:!0,path:"/*",render:a})))},ae=function(e){return l.a.createElement("div",null,l.a.createElement("nav",{className:"navbar navbar-expand-md background navbar-dark"},l.a.createElement("div",{className:"container"},l.a.createElement("a",{className:"navbar-brand header",href:"/"},l.a.createElement("img",{className:"header-logo",src:a(136)}),"PropertyMonopoly"),l.a.createElement("div",{className:"collapse navbar-collapse text-center justify-content-end",id:"mainNavbar"},l.a.createElement("a",{className:"btn navbar-btn background ml-2 text-white",href:"/"},l.a.createElement("i",{className:"fa d-inline fa-lg fa-user-circle-o"}),"Premium"),l.a.createElement("a",{className:"btn navbar-btn background ml-2 text-white",href:"/"},l.a.createElement("i",{className:"fa d-inline fa-lg fa-user-circle-o"}),"About Us"),l.a.createElement("a",{className:"btn navbar-btn background ml-2 text-white",href:"/"},l.a.createElement("i",{className:"fa d-inline fa-lg fa-user-circle-o"}),"Contact Us")))))},ne=function(e){function t(e){return Object(c.a)(this,t),Object(s.a)(this,Object(m.a)(t).call(this,e))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return l.a.createElement("div",{className:"background"},l.a.createElement("div",{className:"container footer-container"},l.a.createElement("div",{className:"row row-pad no-pad-top"},l.a.createElement("div",null))))}}]),t}(l.a.Component),le=function(e){function t(){return Object(c.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"componentDidMount",value:function(){document.title="Jack Tarbox"}},{key:"render",value:function(){return l.a.createElement("div",{className:"bg"},l.a.createElement(p.a,null,l.a.createElement(ae,null),l.a.createElement(te,null),l.a.createElement(ne,null)))}}]),t}(n.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));r.a.render(l.a.createElement(le,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})},17:function(e,t,a){},69:function(e,t,a){e.exports=a(137)},74:function(e,t,a){},75:function(e,t,a){}},[[69,1,2]]]);
//# sourceMappingURL=main.b525c92b.chunk.js.map