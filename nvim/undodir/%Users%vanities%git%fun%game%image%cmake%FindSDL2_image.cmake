Vim�UnDo� ��v���U��;��>2J>�!9�9�k$��>m   d                                   ^S�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ^6K     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^6M    �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^S�     �       f   g       �          f    5�_�                     e        ����                                                                                                                                                                                                                                                                                                                            e           �           V        ^S�    �   d   e       g       L# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying   @# file Copyright.txt or https://cmake.org/licensing for details.       #.rst:   # FindSDL2_image   # -------------   #   # Locate SDL2_image library   #   # This module defines:   #   # ::   #   A#   SDL2_IMAGE_LIBRARIES, the name of the library to link against   6#   SDL2_IMAGE_INCLUDE_DIRS, where to find the headers   :#   SDL2_IMAGE_FOUND, if false, do not try to link against   D#   SDL2_IMAGE_VERSION_STRING - human-readable string containing the   4#                              version of SDL2_image   #   #   #   B# For backward compatibility the following variables are also set:   #   # ::   #   :#   SDL2IMAGE_LIBRARY (same value as SDL2_IMAGE_LIBRARIES)   A#   SDL2IMAGE_INCLUDE_DIR (same value as SDL2_IMAGE_INCLUDE_DIRS)   4#   SDL2IMAGE_FOUND (same value as SDL2_IMAGE_FOUND)   #   #   #   A# $SDLDIR is an environment variable that would correspond to the   4# ./configure --prefix=$SDLDIR used in building SDL.   #   A# Created by Eric Wing.  This was influenced by the FindSDL.cmake   A# module, but with modifications to recognize OS X frameworks and   '# additional Unix paths (FreeBSD, etc).       8if(NOT SDL2_IMAGE_INCLUDE_DIR AND SDL2IMAGE_INCLUDE_DIR)   Q  set(SDL2_IMAGE_INCLUDE_DIR ${SDL2IMAGE_INCLUDE_DIR} CACHE PATH "directory cache   *entry initialized from old variable name")   endif()   ,find_path(SDL2_IMAGE_INCLUDE_DIR SDL_image.h     HINTS       ENV SDL2IMAGEDIR       ENV SDL2DIR       ${SDL2_DIR}     PATH_SUFFIXES SDL2   =                # path suffixes to search inside ENV{SDL2DIR}   $                include/SDL2 include   )       if(CMAKE_SIZEOF_VOID_P EQUAL 8)   !  set(VC_LIB_PATH_SUFFIX lib/x64)   else()   !  set(VC_LIB_PATH_SUFFIX lib/x86)   endif()       0if(NOT SDL2_IMAGE_LIBRARY AND SDL2IMAGE_LIBRARY)   N  set(SDL2_IMAGE_LIBRARY ${SDL2IMAGE_LIBRARY} CACHE FILEPATH "file cache entry   $initialized from old variable name")   endif()   find_library(SDL2_IMAGE_LIBRARY     NAMES SDL2_image     HINTS       ENV SDL2IMAGEDIR       ENV SDL2DIR       ${SDL2_DIR}   )  PATH_SUFFIXES lib ${VC_LIB_PATH_SUFFIX}   )       Nif(SDL2_IMAGE_INCLUDE_DIR AND EXISTS "${SDL2_IMAGE_INCLUDE_DIR}/SDL2_image.h")   �  file(STRINGS "${SDL2_IMAGE_INCLUDE_DIR}/SDL2_image.h" SDL2_IMAGE_VERSION_MAJOR_LINE REGEX "^#define[ \t]+SDL2_IMAGE_MAJOR_VERSION[ \t]+[0-9]+$")   �  file(STRINGS "${SDL2_IMAGE_INCLUDE_DIR}/SDL2_image.h" SDL2_IMAGE_VERSION_MINOR_LINE REGEX "^#define[ \t]+SDL2_IMAGE_MINOR_VERSION[ \t]+[0-9]+$")   �  file(STRINGS "${SDL2_IMAGE_INCLUDE_DIR}/SDL2_image.h" SDL2_IMAGE_VERSION_PATCH_LINE REGEX "^#define[ \t]+SDL2_IMAGE_PATCHLEVEL[ \t]+[0-9]+$")   �  string(REGEX REPLACE "^#define[ \t]+SDL2_IMAGE_MAJOR_VERSION[ \t]+([0-9]+)$" "\\1" SDL2_IMAGE_VERSION_MAJOR "${SDL2_IMAGE_VERSION_MAJOR_LINE}")   �  string(REGEX REPLACE "^#define[ \t]+SDL2_IMAGE_MINOR_VERSION[ \t]+([0-9]+)$" "\\1" SDL2_IMAGE_VERSION_MINOR "${SDL2_IMAGE_VERSION_MINOR_LINE}")   �  string(REGEX REPLACE "^#define[ \t]+SDL2_IMAGE_PATCHLEVEL[ \t]+([0-9]+)$" "\\1" SDL2_IMAGE_VERSION_PATCH "${SDL2_IMAGE_VERSION_PATCH_LINE}")   t  set(SDL2_IMAGE_VERSION_STRING ${SDL2_IMAGE_VERSION_MAJOR}.${SDL2_IMAGE_VERSION_MINOR}.${SDL2_IMAGE_VERSION_PATCH})   &  unset(SDL2_IMAGE_VERSION_MAJOR_LINE)   &  unset(SDL2_IMAGE_VERSION_MINOR_LINE)   &  unset(SDL2_IMAGE_VERSION_PATCH_LINE)   !  unset(SDL2_IMAGE_VERSION_MAJOR)   !  unset(SDL2_IMAGE_VERSION_MINOR)   !  unset(SDL2_IMAGE_VERSION_PATCH)   endif()       /set(SDL2_IMAGE_LIBRARIES ${SDL2_IMAGE_LIBRARY})   6set(SDL2_IMAGE_INCLUDE_DIRS ${SDL2_IMAGE_INCLUDE_DIR})       &include(FindPackageHandleStandardArgs)       ,FIND_PACKAGE_HANDLE_STANDARD_ARGS(SDL2_image   \                                  REQUIRED_VARS SDL2_IMAGE_LIBRARIES SDL2_IMAGE_INCLUDE_DIRS   H                                  VERSION_VAR SDL2_IMAGE_VERSION_STRING)       # for backward compatibility   .set(SDL2IMAGE_LIBRARY ${SDL2_IMAGE_LIBRARIES})   5set(SDL2IMAGE_INCLUDE_DIR ${SDL2_IMAGE_INCLUDE_DIRS})   (set(SDL2IMAGE_FOUND ${SDL2_IMAGE_FOUND})       ;mark_as_advanced(SDL2_IMAGE_LIBRARY SDL2_IMAGE_INCLUDE_DIR)5��