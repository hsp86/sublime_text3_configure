%# ---------------------------------- WARNING ----------------------------------
%#       Do NOT Modify this template, create a new one for customization
%#                It will get overwritten upon update
%#  从github.tpl修改，添加流程图和序列图的支持
%#                                              胡祀鹏
%#                                              2016.09.21
%#  在MarkDown中使用方式如下（当然一个MarkDown文档支持多个多个图）：
%#    <div class="flowchart">
%#      flowchart代码，指定class为flowchart，代码行首不能有空格
%#    </div>
%#    <div class="sequence">
%#      sequence代码，指定class为sequence，代码行首不能有空格
%#    </div>
%# -----------------------------------------------------------------------------
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{filename}}—{{dirname}}</title>
    <link rel="stylesheet" type="text/css" href="/public/github.css">
  </head>
  <body>
    <div class="container">
      <div id="markup">
        <article id="content" class="markdown-body">
          {{!html_part}}
        </article>
      </div>
    </div>
  </body>
  <script type="text/x-omnimarkup-config">
    window.App.Context = {
      buffer_id: {{buffer_id}},
      timestamp: '{{timestamp}}',
      revivable_key: '{{revivable_key}}'
    };
    window.App.Options = {
      ajax_polling_interval: {{ajax_polling_interval}},
      mathjax_enabled: {{'true' if mathjax_enabled else 'false'}}
    };
  </script>
  <script type="text/javascript" src="/public/jquery-2.1.3.min.js"></script>
  <script type="text/javascript" src="/public/imagesloaded.pkgd.min.js"></script>
  <script type="text/javascript" src="/public/app.js"></script>
  <!-- 流程图 -->
  <script src="/public/raphael/raphael.min.js"></script>
  <!-- <script src="/public/raphael/raphael.js"></script> -->
  <script src="/public/flowchart/flowchart.min.js"></script>
  <!-- 序列图 -->
  <!-- <script src="/public/raphael/raphael-min.js"></script> -->
  <script src="/public/underscore/underscore-min.js"></script>
  <script src="/public/sequence/sequence-diagram-min.js"></script>
  %if mathjax_enabled:
  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
          inlineMath: [ ['$','$'], ["\\(","\\)"] ],
          displayMath: [ ['$$', '$$'], ["\\[", "\\]"] ],
          processEscapes: true
        },
        TeX: {
          equationNumbers: {
            autoNumber: 'AMS'
          }
        },
        'HTML-CSS': {
          imageFont: null
        }
      });
  </script>
  <script>
      $(function(){
        $('.flowchart').flowChart();
        // $(".sequence").sequenceDiagram({theme: 'hand'});
        $(".sequence").sequenceDiagram({theme: 'simple'});
      });
  </script>
  <script type="text/javascript" src="/public/mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
  %end
</html>
