Vim�UnDo� ��(����ɏ�]T;Ņa��hL����U�

�J\�   =                                  ^��T    _�                     0       ����                                                                                                                                                                                                                                                                                                                                                             ^�Ȫ     �   /   0          /            const storage = new CloudStorage();5�_�                    0       ����                                                                                                                                                                                                                                                                                                                                                             ^�Ȯ     �   /   1   C      D            await storage.downloadFile(videoFilePath, tempFilePath);5�_�                    0       ����                                                                                                                                                                                                                                                                                                                                                             ^�Ȱ     �   /   1   C      I            await videostorage.downloadFile(videoFilePath, tempFilePath);5�_�                    0       ����                                                                                                                                                                                                                                                                                                                                                             ^�Ȳ     �   /   1   C      I            await videoStorage.downloadFile(videoFilePath, tempFilePath);5�_�                    6       ����                                                                                                                                                                                                                                                                                                                                                             ^���     �   5   7   C      %            await storage.uploadFile(5�_�                    0       ����                                                                                                                                                                                                                                                                                                                                                             ^���    �   /   1   C      M            await videoFullStorage.downloadFile(videoFilePath, tempFilePath);5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^��    �   B   D              );�   A   C          	        }�   @   B                      return;�   ?   A          >            console.log("Completed creating image thumbnail");�   >   @          +            fs.unlinkSync(tempOutFilePath);�   =   ?          (            fs.unlinkSync(tempFilePath);�   <   >           �   ;   =                      );�   :   <                          createAccess�   9   ;                          metadata,�   8   :          !                PNG_CONTENT_TYPE,�   7   9          "                thumbnailFilePath,�   6   8                           tempOutFilePath,�   5   7          4            await imagesThumbnailStorage.uploadFile(�   4   6           �   3   5                      );�   2   4                          tempOutFilePath�   1   3                          tempFilePath,�   0   2          8            await new Ffmpeg().convertMp4ToThumbnailPng(�   /   1          S            await videosThumbnailStorage.downloadFile(videoFilePath, tempFilePath);�   .   0           �   -   /          &            const createAccess = true;�   ,   .          Z            const thumbnailFilePath = `${IMAGE_THUMBNAIL_PATH}${videoId}${PNG_EXTENSION}`;�   +   -          Q            const videoFilePath = `${VIDEO_FULL_PATH}${videoId}${MP4_EXTENSION}`;�   *   ,          R            const tempOutFilePath = path.join(os.tmpdir(), `out${PNG_EXTENSION}`);�   )   +          P            const tempFilePath = path.join(os.tmpdir(), `temp${MP4_EXTENSION}`);�   (   *           �   '   )          H            const videoId: string = metadata ? metadata["videoId"] : "";�   &   (          0            const metadata = object["metadata"];�   %   '          E            console.log("Creating image thumbnail of video", object);�   $   &           �   #   %                      }�   "   $                          return;�   !   #          ,            if (!isVideoThumbnail(object)) {�       "          *        async (object): Promise<void> => {�      !              .onFinalize(�                     .object()�                    .storage.bucket()�                    .runWith(runtimeOpts)�                -export const createImageThumbnail = functions�                 �                 */�                 * clean�                	 * upload�                	 * mutate�                /* donwload�                 �                };�                #    timeoutSeconds: 300, // max=540�                const runtimeOpts = {�                 �                8const IMAGE_THUMBNAIL_PATH = `${IMAGE_PATH}thumbnails/`;�                -const VIDEO_FULL_PATH = `${VIDEO_PATH}full/`;�                const VIDEO_PATH = "videos/";�                const IMAGE_PATH = "images/";�                %const PNG_CONTENT_TYPE = "image/png";�   
             const PNG_EXTENSION = ".png";�   	             const MP4_EXTENSION = ".mp4";�      
           �      	          0import { isVideoThumbnail } from "./validators";�                /import { Ffmpeg } from "../../../utils/ffmpeg";�                <import { CloudStorage } from "../../../utils/cloud_storage";�                 �                0import * as functions from "firebase-functions";�                import * as fs from "fs";�                import * as path from "path";�                 import * as os from "os";5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             ^��    �         C      :import {CloudStorage} from "../../../utils/cloud_storage";5�_�      
           	      5    ����                                                                                                                                                                                                                                                                                                                                                             ^��    �   C            �   B   D              );�   A   C          	        }�   @   B                      return;�   ?   A          >            console.log("Completed creating image thumbnail");�   >   @          +            fs.unlinkSync(tempOutFilePath);�   =   ?          (            fs.unlinkSync(tempFilePath);�   <   >           �   ;   =                      );�   :   <                          createAccess�   9   ;                          metadata,�   8   :          !                PNG_CONTENT_TYPE,�   7   9          "                thumbnailFilePath,�   6   8                           tempOutFilePath,�   5   7          4            await imagesThumbnailStorage.uploadFile(�   4   6           �   3   5                      );�   2   4                          tempOutFilePath�   1   3                          tempFilePath,�   0   2          8            await new Ffmpeg().convertMp4ToThumbnailPng(�   /   1          S            await videosThumbnailStorage.downloadFile(videoFilePath, tempFilePath);�   .   0           �   -   /          &            const createAccess = true;�   ,   .          Z            const thumbnailFilePath = `${IMAGE_THUMBNAIL_PATH}${videoId}${PNG_EXTENSION}`;�   +   -          Q            const videoFilePath = `${VIDEO_FULL_PATH}${videoId}${MP4_EXTENSION}`;�   *   ,          R            const tempOutFilePath = path.join(os.tmpdir(), `out${PNG_EXTENSION}`);�   )   +          P            const tempFilePath = path.join(os.tmpdir(), `temp${MP4_EXTENSION}`);�   (   *           �   '   )          H            const videoId: string = metadata ? metadata["videoId"] : "";�   &   (          0            const metadata = object["metadata"];�   %   '          E            console.log("Creating image thumbnail of video", object);�   $   &           �   #   %                      }�   "   $                          return;�   !   #          ,            if (!isVideoThumbnail(object)) {�       "          *        async (object): Promise<void> => {�      !              .onFinalize(�                     .object()�                    .storage.bucket()�                    .runWith(runtimeOpts)�                -export const createImageThumbnail = functions�                 �                 */�                 * clean�                	 * upload�                	 * mutate�                /* donwload�                 �                };�                #    timeoutSeconds: 300, // max=540�                const runtimeOpts = {�                 �                8const IMAGE_THUMBNAIL_PATH = `${IMAGE_PATH}thumbnails/`;�                -const VIDEO_FULL_PATH = `${VIDEO_PATH}full/`;�                const VIDEO_PATH = "videos/";�                const IMAGE_PATH = "images/";�                %const PNG_CONTENT_TYPE = "image/png";�   
             const PNG_EXTENSION = ".png";�   	             const MP4_EXTENSION = ".mp4";�      
           �      	          .import {isVideoThumbnail} from "./validators";�                -import {Ffmpeg} from "../../../utils/ffmpeg";�                \import {videosThumbnailStorage, imagesThumbnailStorage} from "../../../utils/cloud_storage";�                 �                0import * as functions from "firebase-functions";�                import * as fs from "fs";�                import * as path from "path";�                 import * as os from "os";5�_�   	              
   0   >    ����                                                                                                                                                                                                                                                                                                                                                             ^��6     �   /   1   F      Z            const thumbnailFilePath = `${IMAGE_THUMBNAIL_PATH}${videoId}${PNG_EXTENSION}`;5�_�   
                 0   #    ����                                                                                                                                                                                                                                                                                                                                                             ^��<     �   /   1   F      C            const thumbnailFilePath = `${videoId}${PNG_EXTENSION}`;5�_�                    ;   !    ����                                                                                                                                                                                                                                                                                                                                                             ^��A    �   :   <   F      "                thumbnailFilePath,5�_�                    3   !    ����                                                                                                                                                                                                                                                                                                                                                             ^��R    �   2   4   F      S            await videosThumbnailStorage.downloadFile(videoFilePath, tempFilePath);5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^��]    �         F          videosThumbnailStorage,5�_�                    /       ����                                                                                                                                                                                                                                                                                                                                                             ^��h     �   .   0   F      Q            const videoFilePath = `${VIDEO_FULL_PATH}${videoId}${MP4_EXTENSION}`;5�_�                    /   5    ����                                                                                                                                                                                                                                                                                                                                                             ^��s    �   .   0   F      Q            const videoFilename = `${VIDEO_FULL_PATH}${videoId}${MP4_EXTENSION}`;5�_�                    3   >    ����                                                                                                                                                                                                                                                                                                                                                             ^��   	 �   2   4   F      N            await videosFullStorage.downloadFile(videoFilePath, tempFilePath);5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^�ɐ     �                -const VIDEO_FULL_PATH = `${VIDEO_PATH}full/`;   8const IMAGE_THUMBNAIL_PATH = `${IMAGE_PATH}thumbnails/`;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^�ɑ   
 �                const IMAGE_PATH = "images/";   const VIDEO_PATH = "videos/";5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^�ɘ    �                    /* donwload   	 * mutate   	 * upload    * clean    */5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             ^�"     �         <      ,            if (!isVideoThumbnail(object)) {5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^�*    �   
      <      .import {isVideoThumbnail} from "./validators";5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^��P     �         <    �         <    5�_�                             ����                                                                                                                                                                                                                                                                                                                                                  V        ^��S    �                    const MP4_EXTENSION = ".mp4";   const PNG_EXTENSION = ".png";   %const PNG_CONTENT_TYPE = "image/png";5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^��H     �         <    �         <          const MP4_EXTENSION = ".mp4";   const PNG_EXTENSION = ".png";   %const PNG_CONTENT_TYPE = "image/png";5��