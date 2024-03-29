import pytest

from scts.tracking.domain.models import TrackingEvent


@pytest.fixture
def fake_html():
    return """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<meta http-equiv="X-UA-Compatible" content="IE=EDGE,chrome=1" />
<html lang="pt-br">
<head>
<meta http-equiv="X-UA-Compatible" content="IE=EDGE,chrome=1" />
<meta http-equiv="Content-Language" Content="pt">
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Resultado Rastreamento</title>
<meta name="description" content="[page]" />
<meta name="keywords" content="" />

<!-- AppInternalsXpert BMX Integration Begin -->
<script>
if(!RVBD_EUE){
   var RVBD_EUE={startJS:Number(new Date()),
   clientId:'',appId:1,
   collector:'apmperformance.correios.com.br',
   collectorHttpPort:80, collectorHttpsPort:443,
   sv:'0401',
   ajax:true, sync:true,
   ajaxResponseTime:true};
   (function(){
      var w=window,l=w.addEventListener,m=w.attachEvent,
      d=document,s='script',t='load',o=RVBD_EUE,
      r=(('https:'===d.location.protocol)?
      'https://apmperformance.correios.com.br:443':
      'http://apmperformance.correios.com.br:80')+
      '/jsi/riverbed_appinternals.d.'+
      (o.ajax?'ajax.js':'js'),p=('onpagehide' in w),e=p?'pageshow':t,
      j=d.createElement(s),x=d.getElementsByTagName(s)[0],
      h=function(y){o.ldJS=o.ldJS||new Date();o.per=y?y.persisted:null;},
      i=function(){o.ld=1;};o.cookie=d.cookie;d.cookie=
      '_op_aixPageId=0; path=/; expires='+(new Date(0)).toGMTString();
      o.cookieAfterDelete=d.cookie;j.async=1;j.src=r;
      if(l){l(e,h,false);if(p){l(t,i,false);}}else if(m)
      {m('on'+e,h);if(p){m('on'+t,i);}}
      if(o.sync){d.write('<'+s+' src=\''+r+'\'></'+s+'>');}
      else{x.parentNode.insertBefore(j,x);}
   })();}
</script>
<!-- AppInternalsXpert BMX Integration End -->
<script type="text/javascript">
pageid = '1C658B24-5056-9163-891FB9FC40735A16';
</script>
<noscript>
<p>identificador da página</p>
</noscript>
<base href="/">
<link rel="icon" href="home2014/img/icon.png" type="image/gif"/>

<!-- CSS -->

  <link href="home2014/css/layout.css"  rel="stylesheet"        type="text/css" />
<!-- /CSS --->

</head>
<!--[if lt IE 7]> <body class="ie6"> <![endif]-->
<!--[if IE 7]>    <body class="ie7"> <![endif]-->
<!--[if IE 8]>    <body class="ie8"> <![endif]-->
<!--[if !IE]>-->  <body>             <!--<![endif]-->
<div class="back">
<div class="acessibilidade">
  <div class="wrap">
    <ul>

        <li class="tocontent"> <span class="separator-bar">&nbsp;</span> <a href="javascript:void(0);" onClick="document.location.hash='ancora';" title="Ir para o conte&uacute;do principal da p&aacute;gina">Ir ao  conte&uacute;do</a> </li>
        <li class="font-plus" id="biggerFont"> <a href="javascript:void(0);" title="Aumentar o tamanho da fonte do texto">A</a> </li>
        <li id="defaultFont"> <span class="separator-dot">&nbsp;</span> <a href="javascript:void(0);" title="Retornar a fonte do texto para tamanho padr&atilde;o">Tamanho padr&atilde;o</a> <span class="separator-dot">&nbsp;</span> </li>
        <li class="font-minus" id="smallerFont"> <a href="javascript:void(0);" title="Diminuir o tamanho da fonte do texto">A</a> </li>
        <li class="contrast" id="contrast"> <span class="separator-bar">&nbsp;</span> <a href="javascript:void(0);" title="Modificar para o modo de alto contraste">Contraste</a> <span class="separator-bar">&nbsp;</span> </li>
        <li> <span class="separator-bar">&nbsp;</span> <a href="http://www.correios.com.br/sobre-correios/sustentabilidade/vertente-social/headmouse-e-teclado-virtual/">Teclado Virtual</a> </li>
        <li> <a href="http://www.correios.com.br/sobre-correios/sustentabilidade/vertente-social/headmouse-e-teclado-virtual/" id="txt-headmouse">Headmouse</a></li>

    </ul>
  </div>
</div>
<!-- header --->
<div class="header">
<h1 class="logo float-left"> <a href="http://www.correios.com.br" title="Ir para a página incial" alt="Logo Correios"><img src="home2014/img/layout/logo.png" alt="Ir para a página inicial" title="Ir para a página incial"/></a> </h1>
<div class="acesso_rapido">

  <div class="text-right">

    <a href="http://apps2.correios.com.br/faleconosco/app/index.php">Fale com os Correios</a><br/>
  </div>
  <div class="produtosaz float-right">
    <div class="expo">Outros sites</div>
    <span class="dados abaaz">
    <div class="dadosaz"> <span class="dica"> Acesse a outros sites dos Correios</span><br/>
      <a href="http://www.correios.com.br/para-voce"><b>Correios para você</b></a><br/>
      <a href="http://www.correios.com.br/para-sua-empresa"><b>Correios para sua empresa</b></a><br/>
      <a href="http://www.correios.com.br/sobre-correios"><b>Sobre Correios</b></a><br/>
      <a href="produtosaz/default.cfm?filtro=R/Z"><b>Espaço da Filatelia</b></a><br/>
      <a href="http://blog.correios.com.br/correios"><b>Blog Institucional do Correios</b></a><br/>
      <a href="http://m.correios.com.br"><b>Correios mobile</b></a><br/>
    </div>
    </span> </div>
  <div class="produtosaz float-right">
    <div class="expo" >Correios de A a Z</div>
    <span class="dados abaaz">
    <div class="dadosaz"> <span class="dica"> Escolha pela letra inicial dos nossos produtos, serviços e assuntos.<br/>
      </span><br/>
      <a href="http://www.correios.com.br/a-a-z/"><b>Todos os itens</b></a><br/>
      <a href="http://www.correios.com.br/a-a-z/?filtro=abc"><b>Correios de A-C</b></a><br/>
      <a href="http://www.correios.com.br/a-a-z/?filtro=def"><b>Correios de D-F</b></a><br/>
      <a href="http://www.correios.com.br/a-a-z/?filtro=ghijklmnopq"><b>Correios de G-Q</b></a><br/>
      <a href="http://www.correios.com.br/a-a-z/?filtro=rstuvwxyz"><b>Correios de R-Z</b></a> </div>
    </span> </div>
  </div>
  <!-- acesso rápido -->
  <br class="clr"/>
  </div>
  <div class="tabs">
  <div class="wrap">
    <ul class="tabs-list">
      <li class="current"> <a href="default.cfm">
        <h2>Sistemas</h2>
        </a> </li>
    </ul>
  </div>
<!-- /header --->
<div class="wrap">
<div class="content">
<div class="laminas" style="display: block;">
<div class="column1">
<span class="mver">
<span class="dominio"></span>
<h3>Rastreamento</h3>
<ul>

  <li><a href="sistemas/rastreamento/default.cfm" target="_self" >Rastreamento de objetos</a></li>
  <li><a href="http://globaltracktrace.ptc.post/gtt.web/Search.aspx" target="_self" >Rastreamento de objetos em outros países</a></li>
  <li><a href="https://www.correios.com.br/precisa-de-ajuda/como-rastrear-um-objeto" target="_self" >Como rastrear um objeto</a></li>
  <li><a href="https://www.correios.com.br/precisa-de-ajuda/como-rastrear-um-objeto/siglas-utilizadas-no-rastreamento-de-objeto" target="_self" >Siglas utilizadas no rastreamento de objetos</a></li>
</ul>
</span>
<!-- Fim Menu vertical -->
</div>
<!-- column1 -->
<div class="column2">
<div class="breadcrumb"></div>
<div class="content ">
<a name="ancora"></a>


                                        <div class="tituloimagem">
                                                <h3><span class="codSro"><span>PU</span><span>524</span><span>124</span><span>388</span><span>BR</span></h3>
                                 </div>

                                        <div class="msg">

                                          </div>

                                        <div class="quadroavisos"> SEDEX 12 e do SEDEX Hoje, representa o hor&aacute;rio real da entrega.</p><p>As informa&ccedil;&otilde;es de rastro de objetos registrados ficar&atilde;o dispon&iacute;veis at&eacute; 180 dias ap&oacute;s a data de postagem.</p><h4>Objetos com origem ou destino fora do Brasil</h4><p>O rastreamento para objetos postados no Brasil com c&oacute;digo iniciado por "R" e "C" e terminado com "BR" n&atilde;o &eacute; garantido fora do territ&oacute;rio brasileiro.</p><p>Para esses objetos, os operadores postais de outros pa&iacute;ses podem n&atilde;o disponibilizar e/ou transmitir informa&ccedil;&atilde;o de rastreamento para o Brasil.</p><p>Sendo assim, consultas de rastreamento de objetos podem tamb&eacute;m ser realizadas nos sites dos operadores de destino dispon&iacute;veis no site da UPU - Uni&atilde;o Postal Universal.</p><p><b>Para os objetos postados no Exterior para o Brasil</b>, o servi&ccedil;o contratado pelo remetente na origem determina o n&iacute;vel de informa&ccedil;&atilde;o de rastreamento de objetos em nosso site.</p>

<p>Objetos registrados recebidos do exterior que apresentam código iniciado por "R" não pertencem &agrave; modalidade expressa, portanto não h&aacute; rastreamento ponto a ponto. As informa&ccedil;&otilde;es no sistema de rastreamento para esses objetos "R" incluem apenas os eventos: "recebimento no Brasil", "entrega", "tentativa de entrega" ou "aguardando retirada na unidade responsável". No caso do objeto ser tributado, haver&aacute; os eventos de "encaminhamento para fiscaliza&ccedil;&atilde;o e tributa&ccedil;&atilde;o e "sa&iacute;da da fiscaliza&ccedil;&atilde;o". </p>



<p>O prazo estimado de entrega dos objetos registrados &eacute; de 40 DIAS &Uacute;TEIS a partir da confirma&ccedil;&atilde;o de pagamento dos impostos (se tributado) e do despacho postal. <a href="http://www.correios.com.br/encomendas-logistica/entrega/importacao/prazos-dos-servicos-internacionais-de-importacao" target="_blank">Tabela prazos de entrega</a></p>
            <p>Remessas iniciadas com o c&oacute;digo "UM" n&atilde;o s&atilde;o rastre&aacute;veis no Brasil. Esse c&oacute;digo &eacute; utilizado pelo pa&iacute;s de origem para indicar que a remessa &eacute; pass&iacute;vel de pagamento de imposto de importa&ccedil;&atilde;o no destino.</p> </div>
                                        <div class="ctrlcontent">


                                        <!-- pode ser suspenso: PU524124388BR-true-->
                                <div class="highlightSRO">



                        <!-- imagem:  -->
                                        <div id="imagemhidden"></div>

                                <div display:block><br />
                                          <br />
                                                <br /><br />

                                          <script src="sistemas/rastreamento/js/qrcode.js" type="text/javascript"></script>
                                          <script src="sistemas/rastreamento/js/jquery.qrcode.js" type="text/javascript"></script>
                                </div>
                                </div>
<table class="listEvent sro">
<tr>
<td class="sroDtEvent" valign="top">02/03/2021 <br/>
13:54       <br/>
<label style="text-transform:capitalize;">SAO PAULO / SP</label>
</td>
<td class="sroLbEvent">
<strong>Objeto entregue ao destinatário</strong>
<br/>
</td>
</tr>
</table>
<table class="listEvent sro">
<tr>
<td class="sroDtEvent" valign="top">02/03/2021 <br/>
08:59       <br/>
<label style="text-transform:capitalize;">SAO PAULO / SP</label>
</td>
<td class="sroLbEvent">
<strong>Objeto saiu para entrega ao destinatário</strong>
<br/>
</td>
</tr>
</table>
<table class="listEvent sro">
<tr>
<td class="sroDtEvent" valign="top">02/03/2021 <br/>
05:09       <br/>
SAO PAULO / SP<br/>
</td>
<td class="sroLbEvent">
<strong>Objeto em trânsito - por favor aguarde</strong>
<br/>

de      Unidade de Tratamento
em      SAO PAULO / SP
para    Unidade de Distribuição
em      SAO PAULO / SP<br/>
</td>
</tr>
</table>
<table class="listEvent sro">
<tr>
<td class="sroDtEvent" valign="top">01/03/2021 <br/>
17:57       <br/>
SAO PAULO / SP<br/>
</td>
<td class="sroLbEvent">
<strong>Objeto em trânsito - por favor aguarde</strong>
<br/>

de      Agência dos Correios
em      SAO PAULO / SP
para    Unidade de Tratamento
em      SAO PAULO / SP<br/>
</td>
</tr>
</table>
<table class="listEvent sro">
<tr>
<td class="sroDtEvent" valign="top">01/03/2021 <br/>
17:27       <br/>
<label style="text-transform:capitalize;">SAO PAULO / SP</label>
</td>
<td class="sroLbEvent">
<strong>Objeto postado</strong>
<br/>
</td>
</tr>
</table>






                <br />

                <div id="imagem" style="display:none">
                        <div class="status">

                                  <img src="home2014/img/SRO/" alt="Objeto entregue ao destinatário">

                        </div>

                </div>


                <script>
                        document.getElementById('imagemhidden').innerHTML = document.getElementById('imagem').innerHTML;
                </script>

                <div class="btnform">
                <p>Todos os objetos internacionais estão sujeitos à cobrança do despacho postal. Clique <a href="https://www.correios.com.br/encomendas-logistica/minhas-importacoes">aqui</a> para saber mais</p>


                        <button class="btn2 float-left" onClick="location.href='https://www2.correios.com.br/sistemas/rastreamento/'">Nova Consulta</button>





                </div>
                <br /><br />

                <div class="act-extras" style="display:block; width:430px">



                        <form name="frmprint" id="frmprint" method="post" action="sistemas/rastreamento/newprint.cfm" target="_blank">
                                <input type="hidden" name="objetos" value="PU524124388BR" />
                        </form>
                        <a class="icon print sro" onClick="document.getElementById('frmprint').submit();"><img width="22px" height="22px" src="home2014/img/trans.gif">Imprimir</a>
                        <!-- pode ser suspenso-->
                                <!-- Não está logado, mas passivel de suspensão -->

                                        <a class="icon stop sro" onClick="document.getElementById('formTelaSusp').submit();"><img class="fechar" width="22px" height="22px" src="home2014/img/trans.gif">Suspender Entrega</a>
                                        <form name="formTelaSusp" id="formTelaSusp" method="post" action="sistemas/rastreamento/suspensaoEntrega/dsp/default.cfm">
                                                <input type="hidden" name="ObjAsuspender" id="ObjAsuspender" value="PU524124388BR" />
                                        </form>

                </div>
                <br />


                        <div class="destaque" style="background-color:##eee; width:98%;  display:table; height:auto; padding:10px; margin-bottom:5px;">

                                <div  id="qrcodeTable" style="float:left; width:100px"> <img src="https://chart.apis.google.com/chart?cht=qr&chl=PU524124388BR&chs=116x116"
                alt="PU524124388BR - QR code"/> </div>

                        <div style="float:left; width:200px; padding:10px 13px; font-size:1.3em;"> Acesse o aplicativo dos Correios e leia o c&oacute;digo 2D ao lado. Voc&ecirc; n&atilde;o precisar&aacute; digitar o c&oacute;digo do objeto e poder&aacute; salvar na sua lista de favoritos. </div>
                        <div style="float:left; width:100px; margin:3px;"> <a href="https://itunes.apple.com/us/app/sro-mobile/id998782060?l=pt&ls=1&mt=8" target="_blank"> <img src="home2014/img/sro/Apple-store.png" width="138" height="43" style="border:2px solid #eee"> </a> <a href="https://play.google.com/store/apps/details?id=br.com.correios.srocorreios" target="_blank"> <img src="home2014/img/sro/Google-store.png" width="138" height="43" style="border:2px solid #eee"> </a> </div>

                        </div>

                <br />
                <a href="https://www.correios.com.br/banner-sro/link-banner-sro" target="_blank"><img src="https://www.correios.com.br/banner-sro/banner_sro/" width="480px" height="94px" /></a>
                </div>


                        <div class="modal">
                        <div id="inline_content2" class="inline_content">
        <h3><br />
      <br />
      O status do objeto pesquisado est&aacute; finalizado.<br />N&atilde;o &eacute; poss&iacute;vel solicitar notifica&ccedil;&atilde;o por SMS.</h3>
</div>

<script src="sistemas/rastreamento/js/jquery.validationEngine.js" type="text/javascript"></script>
<script src="sistemas/rastreamento/js/jquery.validationEngine-pt.js" type="text/javascript"></script>
<script>
        //$(document).ready(function(){$("#formSms").validationEngine();});
</script>
                        </div>


                <script type="text/javascript" src="sistemas/rastreamento/js/sro.js"></script>
                <script type="text/javascript" src="sistemas/rastreamento/js/jquery.maskedinput.min.js"></script>
                <script type="text/javascript" src="sistemas/rastreamento/js/MascaraValidacao.js"></script>

        <!-- TipoBD(01) -->

</div>
</div>
<br class="clr" />
</div>
</div>
</div>
</div><!-- class="wrap" -->
<!-- laminas -->
<div class="footer">
  <div class="wrap">

      <div class="column-footer">
        <h3><a target="_blank" href="http://apps2.correios.com.br/faleconosco/app/index.php">Fale Conosco</a></h3>
        <ul>
          <li class="node"><a href="sistemas/falecomoscorreios">Manifestação via Internet</a>
            <ul>
              <li><a href="sistemas/falecomoscorreios">Fale Conosco pelo site</a></li>
            </ul>
          </li>
          <li class="node"> <a href="sistemas/falecomoscorreios">Atendimento telef&ocirc;nico</a>
            <ul>
              <li>3003 0100 (Capitais e Regi&atilde;o Metropolitanas)</li>
              <li>0800 725 7282 (Demais localidades)</li>
              <li>0800 725 0100 (Sugest&otilde;es ou reclama&ccedil;&otilde;es)</li>
              <li>0800 725 0898 (exclusivo para portadores <br/>
                de deficiência auditiva) </li>
              <li>3003 1383 (Informações Banco Postal)</li>
            </ul>
          </li>
          <li class="node"> <a href="sistemas/agencias/">Rede de atendimento</a>
            <ul>
              <li><a href="sistemas/agencias">Consulte endereços e horários de atendimentos <br />
                das agências dos Correios</a></li>
            </ul>
          </li>
          <li class="node"> <a href="http://www.correios.com.br/sobre-correios/fale-com-os-correios/ouvidoria">Ouvidoria</a> </li>
        </ul>
      </div>
      <div class="column-footer">
        <h3><a href="">Portal Correios</a></h3>
        <ul>
          <li><a href="http://www.correios.com.br/sitemap">Mapa do site</a></li>
          <li><a href="sistemas/rastreamento/default.cfm">Rastreamento de objetos</a></li>
          <li><a href="http://www.correios.com.br/correios/sobre-correios/sala-de-imprensa/fale-com-a-assessoria-de-comunicacao">Sala de Imprensa</a></li>
          <li><a href="institucional/concursos/correios/default.cfm">Concursos</a></li>
          <li><a href="http://www.correios.com.br/correios/sobre-correios/patrocinio/patrocinio">Patroc&iacute;nios</a></li>
          <li><a href="http://www.correios.com.br/para-voce/correios-de-a-a-z/contatos-comerciais">Contatos comerciais</a></li>
          <li><a href="http://www.correios.com.br/correios/sobre-correios/a-empresa/carta-de-servicos-ao-cidadao">Carta de servi&ccedil;os ao cidad&atilde;o</a></li>
          <li><a href="http://www.correios.com.br/sobre-correios/fale-com-os-correios/denuncias/denuncias/">Denúncia</a></li>
          <li><a href="http://www.mc.gov.br/">Minist&eacute;rio das Comunica&ccedil;&otilde;es</a></li>
        </ul>
      </div>
      <div class="column-footer">
        <h3><a href="">Outros sites dos Correios</a></h3>
        <ul>
          <li><a href="http://www.correios.com.br/para-voce">Correios para voc&ecirc;</a></li>
          <li><a href="http://www.correios.com.br/para-sua-empresa">Correios para sua empresa</a></li>
          <li><a href="http://www.correios.com.br/sobre-correios">Sobre Correios</a></li>
          <li><a href="http://shopping.correios.com.br/correiosonline">Loja virtual dos Correios</a></li>
          <li><a href="http://blog.correios.com.br/correios">Blog dos Correios</a></li>
          <li><a href="http://blog.correios.com.br/filatelia">Espa&ccedil;o da Filatelia</a></li>
          <li><a href="http://m.correios.com.br/">Correios Mobile</a></li>
          <li><a href="http://www2.correios.com.br/">Sistemas dos Correios</a></li>
        </ul>
      </div>
      <div class="copy"> <a href="http://www.correios.com.br/sobre-correios/fale-com-os-correios/politica-de-privacidade-e-notas-legais/">Pol&iacute;tica de Privacidade e notas legais</a> -  © Copyright  2018 Correios - Todos os direitos reservados. </div>
  </div>
</div>
</div>
<!-- class="back" -->
</body></html>



"""


@pytest.fixture
def fake_invalid_html():
    return """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<meta http-equiv="X-UA-Compatible" content="IE=EDGE,chrome=1" />
<html lang="pt-br">
<head>
<meta http-equiv="X-UA-Compatible" content="IE=EDGE,chrome=1" />
<meta http-equiv="Content-Language" Content="pt">
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Resultado Rastreamento</title>
<meta name="description" content="[page]" />
<meta name="keywords" content="" />

<!-- AppInternalsXpert BMX Integration Begin -->
<script>
if(!RVBD_EUE){
   var RVBD_EUE={startJS:Number(new Date()),
   clientId:'',appId:1,
   collector:'apmperformance.correios.com.br',
   collectorHttpPort:80, collectorHttpsPort:443,
   sv:'0401',
   ajax:true, sync:true,
   ajaxResponseTime:true};
   (function(){
      var w=window,l=w.addEventListener,m=w.attachEvent,
      d=document,s='script',t='load',o=RVBD_EUE,
      r=(('https:'===d.location.protocol)?
      'https://apmperformance.correios.com.br:443':
      'http://apmperformance.correios.com.br:80')+
      '/jsi/riverbed_appinternals.d.'+
      (o.ajax?'ajax.js':'js'),p=('onpagehide' in w),e=p?'pageshow':t,
      j=d.createElement(s),x=d.getElementsByTagName(s)[0],
      h=function(y){o.ldJS=o.ldJS||new Date();o.per=y?y.persisted:null;},
      i=function(){o.ld=1;};o.cookie=d.cookie;d.cookie=
      '_op_aixPageId=0; path=/; expires='+(new Date(0)).toGMTString();
      o.cookieAfterDelete=d.cookie;j.async=1;j.src=r;
      if(l){l(e,h,false);if(p){l(t,i,false);}}else if(m)
      {m('on'+e,h);if(p){m('on'+t,i);}}
      if(o.sync){d.write('<'+s+' src=\''+r+'\'></'+s+'>');}
      else{x.parentNode.insertBefore(j,x);}
   })();}
</script>
<!-- AppInternalsXpert BMX Integration End -->
<script type="text/javascript">
pageid = '1C658B24-5056-9163-891FB9FC40735A16';
</script>
<noscript>
<p>identificador da página</p>
</noscript>
<base href="/">
<link rel="icon" href="home2014/img/icon.png" type="image/gif"/>

<!-- CSS -->

  <link href="home2014/css/layout.css"  rel="stylesheet"        type="text/css" />
<!-- /CSS --->

</head>
<!--[if lt IE 7]> <body class="ie6"> <![endif]-->
<!--[if IE 7]>    <body class="ie7"> <![endif]-->
<!--[if IE 8]>    <body class="ie8"> <![endif]-->
<!--[if !IE]>-->  <body>             <!--<![endif]-->
<div class="back">
<div class="acessibilidade">
  <div class="wrap">
    <ul>

        <li class="tocontent"> <span class="separator-bar">&nbsp;</span> <a href="javascript:void(0);" onClick="document.location.hash='ancora';" title="Ir para o conte&uacute;do principal da p&aacute;gina">Ir ao  conte&uacute;do</a> </li>
        <li class="font-plus" id="biggerFont"> <a href="javascript:void(0);" title="Aumentar o tamanho da fonte do texto">A</a> </li>
        <li id="defaultFont"> <span class="separator-dot">&nbsp;</span> <a href="javascript:void(0);" title="Retornar a fonte do texto para tamanho padr&atilde;o">Tamanho padr&atilde;o</a> <span class="separator-dot">&nbsp;</span> </li>
        <li class="font-minus" id="smallerFont"> <a href="javascript:void(0);" title="Diminuir o tamanho da fonte do texto">A</a> </li>
        <li class="contrast" id="contrast"> <span class="separator-bar">&nbsp;</span> <a href="javascript:void(0);" title="Modificar para o modo de alto contraste">Contraste</a> <span class="separator-bar">&nbsp;</span> </li>
        <li> <span class="separator-bar">&nbsp;</span> <a href="http://www.correios.com.br/sobre-correios/sustentabilidade/vertente-social/headmouse-e-teclado-virtual/">Teclado Virtual</a> </li>
        <li> <a href="http://www.correios.com.br/sobre-correios/sustentabilidade/vertente-social/headmouse-e-teclado-virtual/" id="txt-headmouse">Headmouse</a></li>

    </ul>
  </div>
</div>
<!-- header --->
<div class="header">
<h1 class="logo float-left"> <a href="http://www.correios.com.br" title="Ir para a página incial" alt="Logo Correios"><img src="home2014/img/layout/logo.png" alt="Ir para a página inicial" title="Ir para a página incial"/></a> </h1>
<div class="acesso_rapido">

  <div class="text-right">

    <a href="http://apps2.correios.com.br/faleconosco/app/index.php">Fale com os Correios</a><br/>
  </div>
  <div class="produtosaz float-right">
    <div class="expo">Outros sites</div>
    <span class="dados abaaz">
    <div class="dadosaz"> <span class="dica"> Acesse a outros sites dos Correios</span><br/>
      <a href="http://www.correios.com.br/para-voce"><b>Correios para você</b></a><br/>
      <a href="http://www.correios.com.br/para-sua-empresa"><b>Correios para sua empresa</b></a><br/>
      <a href="http://www.correios.com.br/sobre-correios"><b>Sobre Correios</b></a><br/>
      <a href="produtosaz/default.cfm?filtro=R/Z"><b>Espaço da Filatelia</b></a><br/>
      <a href="http://blog.correios.com.br/correios"><b>Blog Institucional do Correios</b></a><br/>
      <a href="http://m.correios.com.br"><b>Correios mobile</b></a><br/>
    </div>
    </span> </div>
  <div class="produtosaz float-right">
    <div class="expo" >Correios de A a Z</div>
    <span class="dados abaaz">
    <div class="dadosaz"> <span class="dica"> Escolha pela letra inicial dos nossos produtos, serviços e assuntos.<br/>
      </span><br/>
      <a href="http://www.correios.com.br/a-a-z/"><b>Todos os itens</b></a><br/>
      <a href="http://www.correios.com.br/a-a-z/?filtro=abc"><b>Correios de A-C</b></a><br/>
      <a href="http://www.correios.com.br/a-a-z/?filtro=def"><b>Correios de D-F</b></a><br/>
      <a href="http://www.correios.com.br/a-a-z/?filtro=ghijklmnopq"><b>Correios de G-Q</b></a><br/>
      <a href="http://www.correios.com.br/a-a-z/?filtro=rstuvwxyz"><b>Correios de R-Z</b></a> </div>
    </span> </div>
  </div>
  <!-- acesso rápido -->
  <br class="clr"/>
  </div>
  <div class="tabs">
  <div class="wrap">
    <ul class="tabs-list">
      <li class="current"> <a href="default.cfm">
        <h2>Sistemas</h2>
        </a> </li>
    </ul>
  </div>
<!-- /header --->
<div class="wrap">
<div class="content">
<div class="laminas" style="display: block;">
<div class="column1">
<span class="mver">
<span class="dominio"></span>
<h3>Rastreamento</h3>
<ul>

  <li><a href="sistemas/rastreamento/default.cfm" target="_self" >Rastreamento de objetos</a></li>
  <li><a href="http://globaltracktrace.ptc.post/gtt.web/Search.aspx" target="_self" >Rastreamento de objetos em outros países</a></li>
  <li><a href="https://www.correios.com.br/precisa-de-ajuda/como-rastrear-um-objeto" target="_self" >Como rastrear um objeto</a></li>
  <li><a href="https://www.correios.com.br/precisa-de-ajuda/como-rastrear-um-objeto/siglas-utilizadas-no-rastreamento-de-objeto" target="_self" >Siglas utilizadas no rastreamento de objetos</a></li>
</ul>
</span>
<!-- Fim Menu vertical -->
</div>
<!-- column1 -->
<div class="column2">
<div class="breadcrumb"></div>
<div class="content ">
<a name="ancora"></a>


                                        <div class="tituloimagem">
                                                <h3><span class="codSro"><span>PU</span><span>524</span><span>124</span><span>388</span><span>BR</span></h3>
                                 </div>

                                        <div class="msg">

                                          </div>

                                        <div class="quadroavisos"> SEDEX 12 e do SEDEX Hoje, representa o hor&aacute;rio real da entrega.</p><p>As informa&ccedil;&otilde;es de rastro de objetos registrados ficar&atilde;o dispon&iacute;veis at&eacute; 180 dias ap&oacute;s a data de postagem.</p><h4>Objetos com origem ou destino fora do Brasil</h4><p>O rastreamento para objetos postados no Brasil com c&oacute;digo iniciado por "R" e "C" e terminado com "BR" n&atilde;o &eacute; garantido fora do territ&oacute;rio brasileiro.</p><p>Para esses objetos, os operadores postais de outros pa&iacute;ses podem n&atilde;o disponibilizar e/ou transmitir informa&ccedil;&atilde;o de rastreamento para o Brasil.</p><p>Sendo assim, consultas de rastreamento de objetos podem tamb&eacute;m ser realizadas nos sites dos operadores de destino dispon&iacute;veis no site da UPU - Uni&atilde;o Postal Universal.</p><p><b>Para os objetos postados no Exterior para o Brasil</b>, o servi&ccedil;o contratado pelo remetente na origem determina o n&iacute;vel de informa&ccedil;&atilde;o de rastreamento de objetos em nosso site.</p>

<p>Objetos registrados recebidos do exterior que apresentam código iniciado por "R" não pertencem &agrave; modalidade expressa, portanto não h&aacute; rastreamento ponto a ponto. As informa&ccedil;&otilde;es no sistema de rastreamento para esses objetos "R" incluem apenas os eventos: "recebimento no Brasil", "entrega", "tentativa de entrega" ou "aguardando retirada na unidade responsável". No caso do objeto ser tributado, haver&aacute; os eventos de "encaminhamento para fiscaliza&ccedil;&atilde;o e tributa&ccedil;&atilde;o e "sa&iacute;da da fiscaliza&ccedil;&atilde;o". </p>



<p>O prazo estimado de entrega dos objetos registrados &eacute; de 40 DIAS &Uacute;TEIS a partir da confirma&ccedil;&atilde;o de pagamento dos impostos (se tributado) e do despacho postal. <a href="http://www.correios.com.br/encomendas-logistica/entrega/importacao/prazos-dos-servicos-internacionais-de-importacao" target="_blank">Tabela prazos de entrega</a></p>
            <p>Remessas iniciadas com o c&oacute;digo "UM" n&atilde;o s&atilde;o rastre&aacute;veis no Brasil. Esse c&oacute;digo &eacute; utilizado pelo pa&iacute;s de origem para indicar que a remessa &eacute; pass&iacute;vel de pagamento de imposto de importa&ccedil;&atilde;o no destino.</p> </div>
                                        <div class="ctrlcontent">


                                        <!-- pode ser suspenso: PU524124388BR-true-->
                                <div class="highlightSRO">



                        <!-- imagem:  -->
                                        <div id="imagemhidden"></div>

                                <div display:block><br />
                                          <br />
                                                <br /><br />

                                          <script src="sistemas/rastreamento/js/qrcode.js" type="text/javascript"></script>
                                          <script src="sistemas/rastreamento/js/jquery.qrcode.js" type="text/javascript"></script>
                                </div>
                                </div>


                <br />


                <script>
                        document.getElementById('imagemhidden').innerHTML = document.getElementById('imagem').innerHTML;
                </script>

                <div class="btnform">
                <p>Todos os objetos internacionais estão sujeitos à cobrança do despacho postal. Clique <a href="https://www.correios.com.br/encomendas-logistica/minhas-importacoes">aqui</a> para saber mais</p>


                        <button class="btn2 float-left" onClick="location.href='https://www2.correios.com.br/sistemas/rastreamento/'">Nova Consulta</button>





                </div>
                <br /><br />

                <div class="act-extras" style="display:block; width:430px">



                        <form name="frmprint" id="frmprint" method="post" action="sistemas/rastreamento/newprint.cfm" target="_blank">
                                <input type="hidden" name="objetos" value="PU524124388BR" />
                        </form>
                        <a class="icon print sro" onClick="document.getElementById('frmprint').submit();"><img width="22px" height="22px" src="home2014/img/trans.gif">Imprimir</a>
                        <!-- pode ser suspenso-->
                                <!-- Não está logado, mas passivel de suspensão -->

                                        <a class="icon stop sro" onClick="document.getElementById('formTelaSusp').submit();"><img class="fechar" width="22px" height="22px" src="home2014/img/trans.gif">Suspender Entrega</a>
                                        <form name="formTelaSusp" id="formTelaSusp" method="post" action="sistemas/rastreamento/suspensaoEntrega/dsp/default.cfm">
                                                <input type="hidden" name="ObjAsuspender" id="ObjAsuspender" value="PU524124388BR" />
                                        </form>

                </div>
                <br />


                        <div class="destaque" style="background-color:##eee; width:98%;  display:table; height:auto; padding:10px; margin-bottom:5px;">

                                <div  id="qrcodeTable" style="float:left; width:100px"> <img src="https://chart.apis.google.com/chart?cht=qr&chl=PU524124388BR&chs=116x116"
                alt="PU524124388BR - QR code"/> </div>

                        <div style="float:left; width:200px; padding:10px 13px; font-size:1.3em;"> Acesse o aplicativo dos Correios e leia o c&oacute;digo 2D ao lado. Voc&ecirc; n&atilde;o precisar&aacute; digitar o c&oacute;digo do objeto e poder&aacute; salvar na sua lista de favoritos. </div>
                        <div style="float:left; width:100px; margin:3px;"> <a href="https://itunes.apple.com/us/app/sro-mobile/id998782060?l=pt&ls=1&mt=8" target="_blank"> <img src="home2014/img/sro/Apple-store.png" width="138" height="43" style="border:2px solid #eee"> </a> <a href="https://play.google.com/store/apps/details?id=br.com.correios.srocorreios" target="_blank"> <img src="home2014/img/sro/Google-store.png" width="138" height="43" style="border:2px solid #eee"> </a> </div>

                        </div>

                <br />
                <a href="https://www.correios.com.br/banner-sro/link-banner-sro" target="_blank"><img src="https://www.correios.com.br/banner-sro/banner_sro/" width="480px" height="94px" /></a>
                </div>


                        <div class="modal">
                        <div id="inline_content2" class="inline_content">
        <h3><br />
      <br />
      O status do objeto pesquisado est&aacute; finalizado.<br />N&atilde;o &eacute; poss&iacute;vel solicitar notifica&ccedil;&atilde;o por SMS.</h3>
</div>

<script src="sistemas/rastreamento/js/jquery.validationEngine.js" type="text/javascript"></script>
<script src="sistemas/rastreamento/js/jquery.validationEngine-pt.js" type="text/javascript"></script>
<script>
        //$(document).ready(function(){$("#formSms").validationEngine();});
</script>
                        </div>


                <script type="text/javascript" src="sistemas/rastreamento/js/sro.js"></script>
                <script type="text/javascript" src="sistemas/rastreamento/js/jquery.maskedinput.min.js"></script>
                <script type="text/javascript" src="sistemas/rastreamento/js/MascaraValidacao.js"></script>

        <!-- TipoBD(01) -->

</div>
</div>
<br class="clr" />
</div>
</div>
</div>
</div><!-- class="wrap" -->
<!-- laminas -->
<div class="footer">
  <div class="wrap">

      <div class="column-footer">
        <h3><a target="_blank" href="http://apps2.correios.com.br/faleconosco/app/index.php">Fale Conosco</a></h3>
        <ul>
          <li class="node"><a href="sistemas/falecomoscorreios">Manifestação via Internet</a>
            <ul>
              <li><a href="sistemas/falecomoscorreios">Fale Conosco pelo site</a></li>
            </ul>
          </li>
          <li class="node"> <a href="sistemas/falecomoscorreios">Atendimento telef&ocirc;nico</a>
            <ul>
              <li>3003 0100 (Capitais e Regi&atilde;o Metropolitanas)</li>
              <li>0800 725 7282 (Demais localidades)</li>
              <li>0800 725 0100 (Sugest&otilde;es ou reclama&ccedil;&otilde;es)</li>
              <li>0800 725 0898 (exclusivo para portadores <br/>
                de deficiência auditiva) </li>
              <li>3003 1383 (Informações Banco Postal)</li>
            </ul>
          </li>
          <li class="node"> <a href="sistemas/agencias/">Rede de atendimento</a>
            <ul>
              <li><a href="sistemas/agencias">Consulte endereços e horários de atendimentos <br />
                das agências dos Correios</a></li>
            </ul>
          </li>
          <li class="node"> <a href="http://www.correios.com.br/sobre-correios/fale-com-os-correios/ouvidoria">Ouvidoria</a> </li>
        </ul>
      </div>
      <div class="column-footer">
        <h3><a href="">Portal Correios</a></h3>
        <ul>
          <li><a href="http://www.correios.com.br/sitemap">Mapa do site</a></li>
          <li><a href="sistemas/rastreamento/default.cfm">Rastreamento de objetos</a></li>
          <li><a href="http://www.correios.com.br/correios/sobre-correios/sala-de-imprensa/fale-com-a-assessoria-de-comunicacao">Sala de Imprensa</a></li>
          <li><a href="institucional/concursos/correios/default.cfm">Concursos</a></li>
          <li><a href="http://www.correios.com.br/correios/sobre-correios/patrocinio/patrocinio">Patroc&iacute;nios</a></li>
          <li><a href="http://www.correios.com.br/para-voce/correios-de-a-a-z/contatos-comerciais">Contatos comerciais</a></li>
          <li><a href="http://www.correios.com.br/correios/sobre-correios/a-empresa/carta-de-servicos-ao-cidadao">Carta de servi&ccedil;os ao cidad&atilde;o</a></li>
          <li><a href="http://www.correios.com.br/sobre-correios/fale-com-os-correios/denuncias/denuncias/">Denúncia</a></li>
          <li><a href="http://www.mc.gov.br/">Minist&eacute;rio das Comunica&ccedil;&otilde;es</a></li>
        </ul>
      </div>
      <div class="column-footer">
        <h3><a href="">Outros sites dos Correios</a></h3>
        <ul>
          <li><a href="http://www.correios.com.br/para-voce">Correios para voc&ecirc;</a></li>
          <li><a href="http://www.correios.com.br/para-sua-empresa">Correios para sua empresa</a></li>
          <li><a href="http://www.correios.com.br/sobre-correios">Sobre Correios</a></li>
          <li><a href="http://shopping.correios.com.br/correiosonline">Loja virtual dos Correios</a></li>
          <li><a href="http://blog.correios.com.br/correios">Blog dos Correios</a></li>
          <li><a href="http://blog.correios.com.br/filatelia">Espa&ccedil;o da Filatelia</a></li>
          <li><a href="http://m.correios.com.br/">Correios Mobile</a></li>
          <li><a href="http://www2.correios.com.br/">Sistemas dos Correios</a></li>
        </ul>
      </div>
      <div class="copy"> <a href="http://www.correios.com.br/sobre-correios/fale-com-os-correios/politica-de-privacidade-e-notas-legais/">Pol&iacute;tica de Privacidade e notas legais</a> -  © Copyright  2018 Correios - Todos os direitos reservados. </div>
  </div>
</div>
</div>
</body></html>
"""


@pytest.fixture
def tracking_events_dict(
  tracking_code
):
    return [
        {'code': tracking_code, 'date': '02/03/2021 13:54', 'location': 'SAO PAULO / SP', 'description': 'Objeto entregue ao destinatário'},
        {'code': tracking_code, 'date': '02/03/2021 08:59', 'location': 'SAO PAULO / SP', 'description': 'Objeto saiu para entrega ao destinatário'},
        {'code': tracking_code, 'date': '02/03/2021 05:09', 'location': 'SAO PAULO / SP', 'description': 'Objeto em trânsito - por favor aguarde   de Unidade de Tratamento em SAO PAULO / SP para Unidade de Distribuição em SAO PAULO / SP'},
        {'code': tracking_code, 'date': '01/03/2021 17:57', 'location': 'SAO PAULO / SP', 'description': 'Objeto em trânsito - por favor aguarde   de Agência dos Correios em SAO PAULO / SP para Unidade de Tratamento em SAO PAULO / SP'},
        {'code': tracking_code, 'date': '01/03/2021 17:27', 'location': 'SAO PAULO / SP', 'description': 'Objeto postado'}
    ]

@pytest.fixture
def tracking_events_list(
  tracking_code
):
    return [
        TrackingEvent(tracking_code, '02/03/2021 13:54', 'SAO PAULO / SP', 'Objeto entregue ao destinatário'),
        TrackingEvent(tracking_code, '02/03/2021 08:59', 'SAO PAULO / SP', 'Objeto saiu para entrega ao destinatário'),
        TrackingEvent(tracking_code, '02/03/2021 05:09', 'SAO PAULO / SP', 'Objeto em trânsito - por favor aguarde   de Unidade de Tratamento em SAO PAULO / SP para Unidade de Distribuição em SAO PAULO / SP'),
        TrackingEvent(tracking_code, '01/03/2021 17:57', 'SAO PAULO / SP', 'Objeto em trânsito - por favor aguarde   de Agência dos Correios em SAO PAULO / SP para Unidade de Tratamento em SAO PAULO / SP'),
        TrackingEvent(tracking_code, '01/03/2021 17:27', 'SAO PAULO / SP', 'Objeto postado')
    ]

@pytest.fixture
def tracking_code():
    return 'ON769530126BR'
