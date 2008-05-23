<?php
/*
 * Created on 23/05/2008
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */

$messageset=array(
	'packageInfoListInstalled'		=>'%c %z%r/'.INSTALLEDLIGHT.'%p'.VERSIONLIGHT.' %v'.SAFELIGHT.'%s '.INSTALLMATCHLIGHT.'- Aquesta �s la versi� instal�lada'.NORMAL."\n".'    %d'."\n"
	,'packageInfoListOtherInstalled'	=>'%c %z%r/'.INSTALLEDLIGHT.'%p'.VERSIONLIGHT.' %v'.SAFELIGHT.'%s '.NORMAL.INSTALLNOTMATCHLIGHT.'- Una altra versi� instal�lada: %i'.NORMAL."\n".'    %d'."\n"
	,'packageInfoListNotInstalled'		=>'%c %z%r/'.HIGHLIGHT.'%p'.VERSIONLIGHT.' %v'.SAFELIGHT.'%s'.NORMAL."\n".'    %d'."\n"
	,'invalidDirectory'			=>'ERROR: %dir no �s un directori v�lid'."\n"
	,'fileMissing'				=>"\r".HIGHLIGHT.'%file'.INEXISTENTLIGHT.' falta a '.HIGHLIGHT.'%p'.NORMAL."\n"
	,'recomendRootCheckDir'			=>HIGHLIGHT.'==> Es recomana executar --checkdir com a root perqu� els ficheros inaccesibles s�n marcados com a desapareguts.'.NORMAL."\n"
	,'recomendRootOrphans'			=>HIGHLIGHT.'==> Es recomana executar --orphans com a root perqu� els ficheros inaccesibles no s�n processats.'.NORMAL."\n"
	,'wrongColorSet'			=>'ERROR: joc de colors incorrecte. Els jocs de colors disponibles s�n: darkbg, lightbg, nocolor.'."\n"
	,'integrityError'			=>HIGHLIGHT.'FATAL: Error d\'integritat! El paquet est� corrupte! El nom del directori \'%p\' no coincideix amb el nom de la descripci�: %desc_name'.NORMAL."\n"
	,'choosePackages'			=>HIGHLIGHT.'==> Introdueixi el n�mero dels paquets a instal�lar. Separi\'ls amb espais. Exemple: 1 2 5 14'.NORMAL."\n"
	,'callingPacman'			=>'Cridant el pacman... Siusplau, introdueixi la contrasenya de root. (degut a un error a les actualitzacions del kernel sudo no �s usat)'."\n"
	,'callingYaourt'			=>'Cridant el yaourt...'."\n"
	,'nothingToInstall'			=>HIGHLIGHT.'==> Res a instal�lar'.NORMAL."\n"
	,'creatingFileList'			=>'==> Creant la llista d\'arxius'."\n"
	,'reusingFileList'			=>'==> Reutilitzant la llista d\'arxius'."\n"
	,'corruptedFileList'			=>'==> La llista d\'arxius existent est� corrupta. Creant-ne una de nova...'."\n"
	,'ownedFile'				=>'%file'.OWNERLIGHT.' es propietat de %p'.NORMAL.' '.VERSIONLIGHT.'%v'.NORMAL."\n"
	,'ownedFileMissing'			=>INEXISTENTLIGHT.'%file era propietat de %p'.NORMAL.' '.VERSIONLIGHT.'%v'.INEXISTENTLIGHT.', per� ja no existeix! Comprova la integritat del teu sistema!'.NORMAL."\n"
	,'unownedFile'				=>'%file'.UNOWNEDLIGHT.' no t� propietari'.NORMAL."\n"
	,'unownedFileMissing'			=>'%file'.INEXISTENTLIGHT.' no t� propietari, per�, de todas formes, no existeix'.NORMAL."\n"
	,'generatingCache'			=>'==> Generant la TUPAC_CACHE'."\n"
	,'generatingCacheCorrupted'		=>'==> Regenerant la TUPAC_CACHE (base de dades corrupta)'."\n"
	,'generatingCacheTupacUpdated'		=>'==> Regenerant la TUPAC_CACHE (la versi� de la TUPAC_CACHE ha sigut actualitzada)'."\n"
	,'generatingCacheDatabaseUpdated'	=>'==> Regenerant la TUPAC_CACHE (la base de dades ha sigut actualitzada)'."\n"
	,'repoIsGone'				=>'::-   la repo "%r" ja no existeix'."\n"
	,'repoIsUpdated'			=>'::*   la repo "%r" ha sigut actualitzada'."\n"
	,'repoIsNew'				=>'::+   nova repo "%r"'."\n"
	,'removePackage'			=>':::--- treure %p'."\n"
	,'updatePackage'			=>':::*** actualitza %p'."\n"
	,'addPackage'				=>':::+++ afegeix %p'."\n"
	,'recheckingLocal'			=>':::... Tornant a comprovar els paquets instal�lats'."\n"
	,'saving'				=>'::: desant'."\n"
	,'reusingCache'				=>'==> Reutilitzant la TUPAC_CACHE existent'."\n"
	,'cacheNeedRoot'			=>ERRORLIGHT.'ERROR: Par a poder crear el directorio de la TUPAC_CACHE has de ser root. Una cop creat, pots treballar com a usuari normal'.NORMAL."\n"
	,'wrongProxy'				=>'ERROR: El format del proxy ha de ser [host]:[port]. Per treure\'l utilitzi "none"'."\n"
	,'usage'				=>'tupac: Una implementaci� de pacman amb cache. Versi�: '.$GLOBALS['tupac_version']
							."\n".''
							."\n".' �s:'
							."\n".'  tupac [paraula] [paraula] ...      : Buscar i instal�lar paquets que contenguin totes les [paraula]'
							."\n".'  tupac -Ss [paraula] [paraula] ...  : Buscar paquets que contenguin totes les [paraula]'
							."\n".'  tupac -Qo [arxiu] [arxiu] ...      : trobar el propietari de cada [arxiu]'
							."\n".'  tupac --checkdir [directori]       : comprovar la integritat de [directori]'
							."\n".'  tupac --orphans [directori]        : trobar els arxius que no pertanyen a cap paquet'
							."\n".'  tupac                              : nom�s crear la cach�'
							."\n".'  tupac [anything else]              : se li passa al yaourt'
							."\n".'  tupac --set-proxy [host:port|none] : configurar un proxy'
							."\n".''
							."\n".' Modificadores:'
							."\n".'  --safe                             : Nom�s buscar paquets segurs'
							."\n".'  --noaur                            : Nom�s buscar a l\'AUR'
							."\n".'  --noprompt                         : No preguntar res'
							."\n".'  --color [darkbg|lightbg|nocolor]   : Escollir el tema de color'
							."\n".'  --repos repo1,repo2,repo3,...      : Especificar les repos actives'
							."\n".'  --lang [xx_XX|machine]             : Seleccionar l\'idioma'
							."\n"
);
