Vim�UnDo� <9��(Ѓ�80�R���h �<�R�^�u���|�   `   9        await new TikTok().tryGetVideoMetadata(shareLink)   H                          _�A    _�                     H       ����                                                                                                                                                                                                                                                                                                                                                             _�:     �   G   I   b      9        await new TikTok().tryGetVideoMetadata(shareLink)5�_�                    H       ����                                                                                                                                                                                                                                                                                                                                                             _�=    �   G   I   b      5        await TikTok().tryGetVideoMetadata(shareLink)5�_�                     H       ����                                                                                                                                                                                                                                                                                                                                                             _�@    �   `                  return mp4FilePath;   };�   _   a          <    await new Ffmpeg().fixMIME(sourceFilePath, mp4FilePath);�   ^   `          D    const mp4FilePath = path.join(os.tmpdir(), destinationFileName);�   ]   _          ): Promise<string> => {�   \   ^              destinationFileName: string�   [   ]              sourceFilePath: string,�   Z   \          const convertToMP4 = async (�   Y   [           �   X   Z          };�   W   Y              return rawVideoFilePath;�   V   X          ?    await new Downloader().downloadFile(url, rawVideoFilePath);�   U   W          @    const rawVideoFilePath = path.join(os.tmpdir(), "temp.mp4");�   T   V          @const downloadTiktok = async (url: string): Promise<string> => {�   S   U           �   R   T          };�   Q   S              return obj;�   P   R              });�   O   Q          9        else if (obj[key] === undefined) delete obj[key];�   N   P          ,            removeNestedUndefined(obj[key]);�   M   O          5        if (obj[key] && typeof obj[key] === "object")�   L   N          '    Object.keys(obj).forEach((key) => {�   K   M          -const removeNestedUndefined = (obj: any) => {�   J   L           �   I   K          };�   H   J              );�   G   I          3        await TikTok.tryGetVideoMetadata(shareLink)�   F   H          !    return removeNestedUndefined(�   E   G          +): Promise<TikTokScraperVideoMetadata> => {�   D   F              shareLink: string�   C   E          !const getTiktokMetadata = async (�   B   D           �   A   C          };�   @   B              }�   ?   A                  return true;�   >   @              } else {�   =   ?                  return false;�   <   >          -        throw new Error("No data supplied.");�   ;   =              if (!value) {�   :   <          /const isPresent = (value: string): boolean => {�   9   ;           �   8   :              });�   7   9                  });�   6   8          +            tiktokMetadata: tiktokMetadata,�   5   7          #        await snapshot.ref.update({�   4   6          -        // append tiktok metadata to document�   3   5           �   2   4          #        fs.unlinkSync(mp4FilePath);�   1   3          (        fs.unlinkSync(rawVideoFilePath);�   0   2                  // clean up�   /   1           �   .   0          
        );�   -   /          F            getVideoMetadata(tiktokMetadata) // storage asset metadata�   ,   .                      "video/mp4",�   +   -                      mp4FilePath,�   *   ,          '        await videosFullStorage.upload(�   )   +                  // store raw video�   (   *           �   '   )          
        );�   &   (          &            `${tiktokMetadata.id}.mp4`�   %   '                      rawVideoFilePath,�   $   &          /        const mp4FilePath = await convertToMP4(�   #   %                  // convert to mp4�   "   $           �   !   #          
        );�       "          .            tiktokMetadata.videoUrlNoWaterMark�      !          6        const rawVideoFilePath = await downloadTiktok(�                 "        // download original asset�                 �                M        const tiktokMetadata = await getTiktokMetadata(data.funMetadata.url);�                #        // get full tiktok metadata�                 �                (        isPresent(data.funMetadata.url);�                %        const data = snapshot.data();�                #    .onCreate(async (snapshot) => {�                #    .firestore.document(documentId)�                    .runWith(runtimeOpts)�                &export const processTikTok = functions�                 �                ;const documentId = `${videosCollection.name}/{documentId}`;�                 �                };�                #    timeoutSeconds: 300, // max=540�                const runtimeOpts = {�                 �                /import { TikTok } from "../../../utils/tiktok";�                Gimport { videosCollection } from "../../../utils/firestore_collection";�   
             Aimport { getVideoMetadata } from "../../../utils/tiktok_scraper";�   	             Aimport { videosFullStorage } from "../../../utils/cloud_storage";�      
          7import { Downloader } from "../../../utils/downloader";�      	          /import { Ffmpeg } from "../../../utils/ffmpeg";�                Eimport { TikTokScraperVideoMetadata } from "../../../types/metadata";�                 �                0import * as functions from "firebase-functions";�                 �                import * as path from "path";�                import * as os from "os";�                 import * as fs from "fs";5��