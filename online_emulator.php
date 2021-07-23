<!DOCTYPE HTML>
<!--
  Industrious by TEMPLATED
  templated.co @templatedco
  Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->
<html>
  <head>
    <title>BACCO - Password</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <meta name="description" content="" />
    <meta name="keywords" content="" />
    <link rel="stylesheet" href="assets/css/main.css" />
    <script src="https://kit.fontawesome.com/fc01f3d3d3.js" crossorigin="anonymous"></script>
    <script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
  </head>
  <body class="is-preload">

    <!-- Header -->
      <header id="header">
        <a class="logo" href="index.html">Bacco</a>
        <div id="pvt">
          <a href="private.html"><i class="icon fa-lock">&nbsp;</i>login</a>
        </div>
        <nav>
          <a href="#menu">Menu</a>
        </nav>
      </header>

    <!-- Nav -->
    <nav id="menu">
      <ul class="links">
        <li><a href="index.html">Home</a></li>
        <li><a href="bacco.html">About</a></li>
        <li><a href="people.html">People</a></li>
        <li><a href="papers.html">Papers</a></li>
        <li><a href="outreach.html">Outreach</a></li>
        <li><a href="data.html">Data</a></li>
        <li><a href="webres.html">WEB resources</a></li>
        <li><a href="contacts.html">Contacts</a></li>
        <li><a href="jobs.html">Job positions</a></li>
      </ul>
    </nav>

    <!-- Heading -->
      <div id="heading" >
        <h1>Online Emulator</h1>
      </div>

    <!-- Main -->
      <section id="main" class="wrapper">
        <div class="inner">
          <div class="content" align="center">

            <?php
            $html_template = '<form action="" method="post">
            <label for="omegacdm">Omega cold dark matter</label>
            <input type="range" value="{VALUE_OCDM}" min="0.2" max="0.4" step="0.01" id="omegacdm" style="background: #d3d3d3" onchange=update_plot()>
            </form>';

            $ocdm = (array_key_exists("Omega_cdm", $_POST)) ? $_POST["Omega_cdm"] : "";
            $cmd_str = "python3 bacco_compute_pk.py " . $ocdm;
            $pyout = shell_exec($cmd_str);

            $html_output = str_replace("{VALUE_OCDM}", $ocdm, $html_template);

            echo $html_output
            ?>

            <div id="tester" style="width:70%;height:100%;"></div>

          </div>
        </div>
      </section>

      <!-- Footer -->
        <div id="includedFooter"></div>

      <script>

        function plot()
        {
          var jsonstr = <?php echo json_encode($pyout) ?>;
          var obj = JSON.parse(jsonstr);

          var trace1 = {
            x: obj.k,
            y: obj.pk,
            type: 'lines',
            line: {width: 3}
          };

          var data = [trace1];

          var layout = {
            title: 'Test this Pk',
            xaxis : {title: 'k',
                    type: 'log',
                    autorange: true
                    },
            yaxis : {title: 'Pk',
                    type: 'log',
                    autorange: true
                    },
            showlegend: false
          };

          Plotly.newPlot('tester', data, layout);
        }
        plot();

        function update_plot()
        {
          <?php
            $ocdm = (array_key_exists("Omega_cdm", $_POST)) ? $_POST["Omega_cdm"] : "";
            $cmd_str = "python3 bacco_compute_pk.py " . $ocdm;
            $pyout = shell_exec($cmd_str);
          ?>
          // plot();
          var trace1 = {
            x: [1,10,100],
            y: [1,10,100],
            type: 'lines',
            line: {width: 3}
          };
          var data = [trace1];
          var layout = {title: <?php echo json_encode($ocdm) ?>};
          Plotly.newPlot('tester', data, layout);
        }
      </script>

  </body>
</html>
