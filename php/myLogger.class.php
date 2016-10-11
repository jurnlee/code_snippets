<?php

class myLogger
{
	public function wxtracers($fileName){
		self::logger($fileName,"remote_addr: ".$_SERVER['REMOTE_ADDR']);
		self::logger($fileName,"query_string: ".$_SERVER['QUERY_STRING']);
	}

	public function logger($fileName,$content){
		$word = date("y-m-d H:i:s  ").$content."[end]<br> \n";
		self::writeLog($fileName,$word);
		
	}

	public function writeLog($fileName,$content){
		/*
		方式一：
		$old = "";
		if (file_exists("wxlog.html")) {
			//$old = file_get_contents("wxlog.html");
		}
		file_put_contents("wxlog.html", $old.date("y-m-d H:i:s ").$content."<br>");
		*/
	
		if (!file_exists($fileName)) {
			file_put_contents($fileName,"开始记录日志： <br /> \n");
		}
		$fo = fopen($fileName, "a");
		fwrite($fo, $content);
		fclose($fo);
	}
	
}
	
?>