import{o as r,c as p,a as t,b as o,t as e,u as n,j as _,d as f,e as y,f as b,g as s,w as c,F as w,B as k,_ as v,h as x,A as B,i as A,k as V}from"./index-4a0b41ef.js";const j="/assets/favicon-a28520da.ico",C="/assets/john-313c2544.jpg",T={class:"markdown-body"},N=t("h2",null,"通辽宇宙地图",-1),$=t("p",null,"作为小约翰可汗的歌迷，为可汗献图大家可以理解吧。",-1),F=t("h3",null,"通辽宇宙基本信息",-1),L=t("p",null,[t("strong",null,"通辽宇宙首府："),o(" 内蒙古通辽市")],-1),S=t("p",null,[t("img",{src:j,alt:"通辽宇宙地图"})],-1),D=t("strong",null,"最高领导人：",-1),I=t("strong",null,"最高领导人称号：",-1),E=t("p",null,[t("img",{src:C,alt:"耗子头像"})],-1),H=t("strong",null,"最高领导人生日：",-1),J=t("strong",null,"最高领导人性别：",-1),K=t("p",null,"我们伟大至高的通辽大可汗处于昏君与明君的叠加态，他的统治并不是完美的，但是他的统治是伟大的，他的统治是光辉的，他的统治是不可替代的。当小约翰更新时进行观测，此时约翰处于明君态，获得“可汗勤政”、“The Supreme King, Little John Come Back To His Loyal Bilibili”等等诸多正面Buff，持续一到两周。当小约翰不更新时进行观测，此时约翰处于昏君态，此时民间风评开始下降，刁民们将在各个平台上催更，“死耗子快更新”是刁民们的常用催更用语。",-1),O=t("p",null,[t("strong",null,"通辽宇宙面积："),o(" 和地球一样大。")],-1),R=t("strong",null,"通辽宇宙人口：",-1),Y=f("<p><strong>通辽宇宙基本面积单位：</strong> 通辽，记作T，通辽，简写T，总面积59535平方千米。</p><p><strong>通辽宇宙基本人口单位：</strong> 大单位：天通苑，约50万人；小单位：回龙观，约30万人。</p><h3>本站技术分析</h3><p>总的来说，项目包括数据获取与数据展示部分。其中工作量主要在界面绘制与数据整理。</p><h4>界面部分</h4><p>界面使用echarts + vue + antdv处理。echarts主要用来处理大地图展示地图geo数据，antdv提供界面组件。地图展示有我们自己标注的数据需要手动渲染处理一下。</p><h4>数据部分</h4><p>数据包括两个，一是up主小约翰可汗的视频数据与up信息数据的爬取与整理，二是世界地图数据的获取与整理。视频信息与up可以通过接口爬取，这里使用了python写了一个爬虫工具将数据存在json文件了，但是直接获取到的数据是不能直接使用的，需要识别出视频内容讲的是什么人什么国家什么组织，有的视频会在视频简介中写明，有些则没有，一个通用的方式是，提取视频语音转成文字后交给AI提取主题，但是这个硬件要求太高了，我这个办公本显然不能胜任，最后还是选择手动补全。地图数据网上是可以找到的，但是通辽、回龙观与天通苑是需要自己手动标注的，于是自己标了一下，非专业人士，所以不太美观。</p>",8),q={__name:"About",setup(u,{expose:a}){return a({frontmatter:{}}),(l,i)=>(r(),p("div",T,[N,$,F,L,S,t("p",null,[D,o(" "+e(n(_).name),1)]),t("p",null,[I,o(" "+e(n(_).title),1)]),E,t("p",null,[H,o(" "+e(n(_).birthday),1)]),t("p",null,[J,o(e(n(_).sex),1)]),K,O,t("p",null,[R,o(" "+e(n(_).follower),1)]),Y]))}},z={class:"header"},G={class:"article"},M={class:"footer"},P=y({__name:"AboutView",setup(u){const a=b();return(h,l)=>{const i=k,d=v,g=A,m=x;return r(),p(w,null,[t("header",z,[s(i,{type:"primary",ghost:"",onClick:l[0]||(l[0]=()=>n(a).go(-1))},{default:c(()=>[s(n(B)),o(" 回到地图")]),_:1})]),t("main",G,[s(n(q))]),t("footer",M,[o("© Copyright "),s(d,{href:"https://www.lishiyuan.cn/",target:"_blank"},{default:c(()=>[o("lishiyuan")]),_:1}),o(" "+e(new Date().getFullYear())+". ",1)]),s(m,{shape:"circle"},{default:c(()=>[s(g,{"visibility-height":0})]),_:1})],64)}}});const U=V(P,[["__scopeId","data-v-5175eec7"]]);export{U as default};
//# sourceMappingURL=AboutView-2cf40e5c.js.map