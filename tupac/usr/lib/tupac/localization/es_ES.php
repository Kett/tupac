<?php
/*
 * Created on 23/05/2008
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */
$messageset=array(
	'packageInfoListInstalled'		=>'%c %z%r/'.INSTALLEDLIGHT.'%p'.VERSIONLIGHT.' %v'.SAFELIGHT.'%s '.INSTALLMATCHLIGHT.'- Esta es la versi�n instalada'.NORMAL."\n".'    %d'."\n"
	,'packageInfoListOtherInstalled'	=>'%c %z%r/'.INSTALLEDLIGHT.'%p'.VERSIONLIGHT.' %v'.SAFELIGHT.'%s '.NORMAL.INSTALLNOTMATCHLIGHT.'- Otra versi�n instalada: %i'.NORMAL."\n".'    %d'."\n"
	,'packageInfoListNotInstalled'		=>'%c %z%r/'.HIGHLIGHT.'%p'.VERSIONLIGHT.' %v'.SAFELIGHT.'%s'.NORMAL."\n".'    %d'."\n"
	,'invalidDirectory'			=>'ERROR: %dir no es un directorio v�lido'."\n"
	,'fileMissing'				=>"\r".HIGHLIGHT.'%file'.INEXISTENTLIGHT.' falta en '.HIGHLIGHT.'%p'.NORMAL."\n"
	,'recomendRootCheckDir'			=>HIGHLIGHT.'==> Se recomienda ejecutar --checkdir como root porque los ficheros inaccesibles son marcados como desaparecidos.'.NORMAL."\n"
	,'recomendRootOrphans'			=>HIGHLIGHT.'==> Se recomienda ejecutar --orphans como root porque los ficheros inaccesibles no son procesados.'.NORMAL."\n"
	,'wrongColorSet'			=>'ERROR: juego de colores incorrecto. Los juegos de colores disponibles son: darkbg, lightbg, nocolor.'."\n"
	,'integrityError'			=>HIGHLIGHT.'FATAL: Error de inegridad! El paquete est� corrupto! El nombre del directorio \'%p\' no coincide con el nombre de la descripci�n: %desc_name'.NORMAL."\n"
	,'choosePackages'			=>HIGHLIGHT.'==> Introduzca el n�mero de los paquetes a instalar. Sep�relos con espacios. Ejemplo: 1 2 5 14'.NORMAL."\n"
	,'callingPacman'			=>'Llamando a pacman... Por favor, introduzca el password de root. (debido a un fallo en las actualizaciones del kernel sudo no es usado)'."\n"
	,'callingYaourt'			=>'Llamando a yaourt...'."\n"
	,'nothingToInstall'			=>HIGHLIGHT.'==> Nada que instalar'.NORMAL."\n"
	,'creatingFileList'			=>'==> Creando la lista de archivos'."\n"
	,'reusingFileList'			=>'==> Reutilizando la lista de archivos'."\n"
	,'corruptedFileList'			=>'==> La lista de archivos existente est� corrupta. Creando una nueva...'."\n"
	,'ownedFile'				=>'%file'.OWNERLIGHT.' es propiedad de %p'.NORMAL.' '.VERSIONLIGHT.'%v'.NORMAL."\n"
	,'ownedFileMissing'			=>INEXISTENTLIGHT.'%file era propiedad de %p'.NORMAL.' '.VERSIONLIGHT.'%v'.INEXISTENTLIGHT.', pero ya no existe! Comprueba la integridad de tu sistema!'.NORMAL."\n"
	,'unownedFile'				=>'%file'.UNOWNEDLIGHT.' no tiene propietario'.NORMAL."\n"
	,'unownedFileMissing'			=>'%file'.INEXISTENTLIGHT.' no tiene propietario, pero, de todas formas, no existe'.NORMAL."\n"
	,'generatingCache'			=>'==> Generando la TUPAC_CACHE'."\n"
	,'generatingCacheCorrupted'		=>'==> Regenerando la TUPAC_CACHE (base de datos corrupta)'."\n"
	,'generatingCacheTupacUpdated'		=>'==> Regenerando la TUPAC_CACHE (la versi�n de TUPAC_CACHE ha sido actualizada)'."\n"
	,'generatingCacheDatabaseUpdated'	=>'==> Regenerando la TUPAC_CACHE (la base de datos ha sido actualizada)'."\n"
	,'repoIsGone'				=>'::-   la repo "%r" ya no existe'."\n"
	,'repoIsUpdated'			=>'::*   la repo "%r" ha sido actualizada'."\n"
	,'repoIsNew'				=>'::+   nueva repo "%r"'."\n"
	,'removePackage'			=>':::--- quitar %p'."\n"
	,'updatePackage'			=>':::*** actualiza %p'."\n"
	,'addPackage'				=>':::+++ a�ade %p'."\n"
	,'recheckingLocal'			=>':::... Volviendo a comprovar los paquetes instalados'."\n"
	,'saving'				=>'::: guardando'."\n"
	,'reusingCache'				=>'==> Reutilizando la TUPAC_CACHE existente'."\n"
	,'cacheNeedRoot'			=>ERRORLIGHT.'ERROR: Para poder crear el directorio de TUPAC_CACHE tienes que ser root. Una vez creado, puedes trabajar como usuario normal'.NORMAL."\n"
	,'wrongProxy'				=>'ERROR: El format del proxy debe ser [host]:[puerto]. Para quitarlo usar "none"'."\n"
	,'usage'				=>'tupac: Una implementaci�n de pacman con cache. Versi�n: '.$GLOBALS['tupac_version']
							."\n".''
							."\n".' Uso:'
							."\n".'  tupac [palabra] [palabra] ...      : Buscar e instalar paquetes que contengan todas las [palabra]'
							."\n".'  tupac -Ss [palabra] [palabra] ...  : Buscar paquetes que contengan todas las [palabra]'
							."\n".'  tupac -Qo [archivo] [archivo] ...  : encontrar el propietario de cada [archivo]'
							."\n".'  tupac --checkdir [directorio]      : verificar la integridad de [directorio]'
							."\n".'  tupac --orphans [directorio]       : encontrar archivos que no pertenecen a ning�n paquete'
							."\n".'  tupac                              : solo crear la cach�'
							."\n".'  tupac [anything else]              : se le passa a yaourt'
							."\n".'  tupac --set-proxy [host:port|none] : configurar un proxy'
							."\n".''
							."\n".' Modificadores:'
							."\n".'  --safe                             : Solo buscar paquetes seguros'
							."\n".'  --noaur                            : No buscar en AUR'
							."\n".'  --noprompt                         : No preguntar nada'
							."\n".'  --color [darkbg|lightbg|nocolor]   : Elegir el tema de color'
							."\n".'  --repos repo1,repo2,repo3,...      : Especificar las repos activas'
							."\n".'  --lang [xx_XX|machine]             : Seleccionar idioma'
							."\n"
);
