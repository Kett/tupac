#!/usr/bin/php -n
<?php

if (dirname(__FILE__)=='/usr/bin') {
	$GLOBALS['include_path']='/usr/lib/tupac/';
	include '/usr/lib/tupac/tupac.inc.php';
	include '/usr/lib/tupac/localization.inc.php';
} else {
	$GLOBALS['include_path']='usr/lib/tupac/';
	include 'usr/lib/tupac/tupac.inc.php';
	include 'usr/lib/tupac/localization.inc.php';
}

if ($GLOBALS['die']) {
	sendMessage($GLOBALS['die'],array());
	exit;
}

if (count($argv)==1) {
	checkCache();
	exit;
}

switch ($argv[1]) {
	case '-Qo':
		checkCache();
		$argv_count=count($argv);
		for ($i=2; $i<$argv_count; $i++)
			$GLOBALS['data']->findFileOwner($argv[$i]);
		break;
	case '-Ss':
		checkCache();
		$GLOBALS['NO_PROMP']=true;
		$parms=$argv;
		array_splice($parms,0,2);
		$GLOBALS['data']->searchByPackageNameAndDescription($parms);
		break;
	case '--checkdir':
		checkCache();
		$GLOBALS['data']->checkDirectory($argv[2]);
		break;
	case '--orphans':
		checkCache();
		PacmanData::findUnownedFiles($argv[2]);
		break;
	case '--console':
		checkCache();
		echo "u: update cache\n";
		echo "s [word] [word] ...: search words omiting aur\n";
		echo "sa [word] [word] ...: search words including aur\n";
		echo "sp [word] [word] ...: search words omiting aur. prompt what to install\n";
		echo "spa [word] [word] ...: search words including aur. prompt what to install\n";
		echo "i [number] [number] ...: isntall result numbers from last search\n";
		echo "exit: exit console\n";
		while (true) {
			$input=split(' ', trim(readline('$ ')));
			switch($input[0]) {
				case 'u':
					checkCache();
					break;
				case 's':
					$GLOBALS['NO_PROMP']=true;
					$GLOBALS['NO_AUR']=true;
					array_splice($input,0,1);
					$GLOBALS['data']->searchByPackageNameAndDescription($input);
					break;
				case 'sa':
					$GLOBALS['NO_PROMP']=true;
					$GLOBALS['NO_AUR']=false;
					array_splice($input,0,1);
					$GLOBALS['data']->searchByPackageNameAndDescription($input);
					break;
				case 'sp':
					$GLOBALS['NO_PROMP']=false;
					$GLOBALS['NO_AUR']=true;
					array_splice($input,0,1);
					$GLOBALS['data']->searchByPackageNameAndDescription($input);
					break;
				case 'spa':
					$GLOBALS['NO_PROMP']=false;
					$GLOBALS['NO_AUR']=false;
					array_splice($input,0,1);
					$GLOBALS['data']->searchByPackageNameAndDescription($input);
					break;
				case 'exit':
					exit;
					break;
				default:
					echo 'Unknow command: '.$input[0]."\n";
					break;
			}
		}
		break;
	default:
		if (substr($argv[1],0,1)=='-') {
			array_splice($argv,0,1);
			call( 'yaourt '.join(' ',$argv) );
		} else {
			checkCache();
			$parms=$argv;
			array_splice($parms,0,1);
			$GLOBALS['data']->searchByPackageNameAndDescription($parms);
		}
		break;
}
