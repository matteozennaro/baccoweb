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
        <h1>Change password</h1>
      </div>

    <!-- Main -->
      <section id="main" class="wrapper">
        <div class="inner">
          <div class="content" align="center">
            <form name="frmChange" method="post" action="" onSubmit="return validatePassword()">
              <div class="message"><?php if(isset($message)) { echo $message; } ?></div>
              <table class="cleant">
                <tr>
                  <td align="right" width="30%">Username</td>
                  <td><input type="text" name="user" class="txtField"/><span id="user"  class="required"></span></td>
                </tr>
                <tr>
                  <td align="right" width="30%">Old Password</td>
                  <td><input type="password" name="oldPassword" class="txtField"/><span id="oldPassword"  class="required"></span></td>
                </tr>
                <tr>
                  <td align="right" width="30%">New Password</td>
                  <td><input type="password" name="newPassword" class="txtField"/><span id="newPassword"  class="required"></span></td>
                </tr>
                <tr>
                  <td align="right" width="30%">Confirm Password</td>
                  <td><input type="password" name="confirmPassword" class="txtField"/><span id="confirmPassword"  class="required"></span></td>
                </tr>
                <tr>
                  <td colspan="2" align="right"><input type="submit" name="submit" value="Submit" class="btnSubmit"></td>
                </tr>
              </table>
            </form>

            <?php
            // APR1-MD5 encryption method (windows compatible)
            function crypt_apr1_md5($plainpasswd, $salt)
            {
                $tmp = "";
                $len = strlen($plainpasswd);
                $text = $plainpasswd.'$apr1$'.$salt;
                $bin = pack("H32", md5($plainpasswd.$salt.$plainpasswd));
                for($i = $len; $i > 0; $i -= 16) { $text .= substr($bin, 0, min(16, $i)); }
                for($i = $len; $i > 0; $i >>= 1) { $text .= ($i & 1) ? chr(0) : $plainpasswd{0}; }
                $bin = pack("H32", md5($text));
                for($i = 0; $i < 1000; $i++)
                {
                    $new = ($i & 1) ? $plainpasswd : $bin;
                    if ($i % 3) $new .= $salt;
                    if ($i % 7) $new .= $plainpasswd;
                    $new .= ($i & 1) ? $bin : $plainpasswd;
                    $bin = pack("H32", md5($new));
                }
                for ($i = 0; $i < 5; $i++)
                {
                    $k = $i + 6;
                    $j = $i + 12;
                    if ($j == 16) $j = 5;
                    $tmp = $bin[$i].$bin[$k].$bin[$j].$tmp;
                }
                $tmp = chr(0).chr(0).$bin[11].$tmp;
                $tmp = strtr(strrev(substr(base64_encode($tmp), 2)),
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
                "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");

                return "$"."apr1"."$".$salt."$".$tmp;
            }

            function get_htpasswd ( $passwdFile, $username )
            {
                $lines = file($passwdFile);
                foreach ($lines as $line)
                {
                    $arr = explode(":", $line);
                    $fileUsername = $arr[0];
                    if ($fileUsername == $username)
                    {
                        $filePasswd = trim($arr[1]);
                        return $filePasswd;
                    }
                }
                return false;
            }

            function matches($password, $filePasswd)
            {
                if (strpos($filePasswd, '$apr1') === 0)
                {
                    // MD5
                    $passParts = explode('$', $filePasswd);
                    $salt = $passParts[2];
                    $hashed = crypt_apr1_md5($password, $salt);
                    return $hashed == $filePasswd;
                }
                elseif (strpos($filePasswd, '{SHA}') === 0)
                {
                    // SHA1
                    $hashed = "{SHA}" . base64_encode(sha1($password, TRUE));
                    return $hashed == $filePasswd;
                }
                elseif (strpos($filePasswd, '$2y$') === 0)
                {
                   // Bcrypt
                   return password_verify ($password, $filePasswd);
                }
                else
                {
                    // Crypt
                    $salt = substr($filePasswd, 0, 2);
                    $hashed = crypt($password, $salt);
                    return $hashed == $filePasswd;
                }
                return false;
            }

            session_start();

            if (count($_POST) > 0) {

              $username = $_POST['user'];
              $password = $_POST['oldPassword'];

              $filePasswd = get_htpasswd( '/home/bacco/.htpasswd', $username );

              if ( matches($password, $filePasswd) )
              {
                  // echo "Correct password\n";
                  // $message = "Correct password";
                  // $result = shell_exec("htpasswd -b /home/bacco/.htpasswd $_POST['user'] $_POST['newPassword']");
                  echo "Password changed\n";
                  $message = "Password changed";
                  $fp = fopen('/home/bacco/try.txt', 'w');
                  fwrite($fp, '1');
                  fwrite($fp, '23');
                  fclose($fp);

              }
              else
              {
                  echo "Incorrect username or password\n";
                  $message = "Incorrect username or password";
              }
            }
            ?>

            </div>
          </div>
        </div>
      </section>

      <!-- Footer -->
        <div id="includedFooter"></div>

    <!-- Scripts -->
      <script src="assets/js/jquery.min.js"></script>
      <script src="assets/js/browser.min.js"></script>
      <script src="assets/js/breakpoints.min.js"></script>
      <script src="assets/js/util.js"></script>
      <script src="assets/js/main.js"></script>
      <script> $(function(){$("#includedFooter").load("footer.html");});</script>
      <script> $(function(){$("#includedMenu").load("menu.html");});</script>
      <script>
      function validatePassword() {
        var username,oldPassword,newPassword,confirmPassword,output = true;

        oldPassword = document.frmChange.oldPassword;
        newPassword = document.frmChange.newPassword;
        confirmPassword = document.frmChange.confirmPassword;

        if(!oldPassword.value) {
        currentPassword.focus();
        document.getElementById("oldPassword").innerHTML = "required";
        output = false;
        }
        else if(!newPassword.value) {
        newPassword.focus();
        document.getElementById("newPassword").innerHTML = "required";
        output = false;
        }
        else if(!confirmPassword.value) {
        confirmPassword.focus();
        document.getElementById("confirmPassword").innerHTML = "required";
        output = false;
        }
        if(newPassword.value != confirmPassword.value) {
        newPassword.value="";
        confirmPassword.value="";
        newPassword.focus();
        document.getElementById("confirmPassword").innerHTML = "passwords do not match!";
        output = false;
        }
        return output;
      }
      </script>

      <?php
        // session_start();
        //
        // if (count($_POST) > 0) {
        //
        //   // This checks if the current password is correct
        //   $result = $result = shell_exec("htpasswd -vb /home/bacco/.htpasswd $_POST['user'] $_POST['newPassword']");
        //
        //   if ($result == 1) {
        //     $result = shell_exec("htpasswd -b /home/bacco/.htpasswd $_POST['user'] $_POST['newPassword']");
        //     $message = "Password changed";
        //   } else
        //     $message = "Current password is not correct";
        // }
      ?>

  </body>
</html>
