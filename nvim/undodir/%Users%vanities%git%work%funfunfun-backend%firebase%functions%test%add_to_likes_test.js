Vim�UnDo� �x�o�fW^f���PkV�s�����4V   -                                  ^��z    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ^��     �      !   G      !    console.log = function () {};5�_�                    '       ����                                                                                                                                                                                                                                                                                                                                                             ^��
    �   &   (   G          delete console.log;5�_�                    B       ����                                                                                                                                                                                                                                                                                                                                                             ^�ջ     �   A   C   G              url: downloadUrl1,5�_�                    B       ����                                                                                                                                                                                                                                                                                                                                                             ^�ռ    �   A   C   G              videourl: downloadUrl1,5�_�                    B       ����                                                                                                                                                                                                                                                                                                                                                             ^���     �   B   D   G    �   B   C   G    5�_�                    C       ����                                                                                                                                                                                                                                                                                                                                                             ^���    �   B   D   H              videoUrl: downloadUrl1,5�_�                    .       ����                                                                                                                                                                                                                                                                                                                                                             ^��    �   -   /   H      .        name: `videos/thumbnails/${videoId1}`,5�_�      	              0       ����                                                                                                                                                                                                                                                                                                                                                             ^��M     �   /   1   H      !        contentType: "video/mp4",5�_�      
           	   0       ����                                                                                                                                                                                                                                                                                                                                                             ^��Q    �   /   1   H      !        contentType: "image/mp4",5�_�   	              
   +   /    ����                                                                                                                                                                                                                                                                                                                                                             ^�ֵ     �   +   -   I            �   +   -   H    5�_�   
                 ,       ����                                                                                                                                                                                                                                                                                                                                                             ^�ַ    �   +   ,                conso5�_�                    8   	    ����                                                                                                                                                                                                                                                                                                                            .   $       7           V   $    ^���     �   8   C   H    �   8   9   H    5�_�                    B       ����                                                                                                                                                                                                                                                                                                                            .   $       7           V   $    ^���   	 �   B   D   S      
          �   B   D   R    5�_�                    @       ����                                                                                                                                                                                                                                                                                                                            .   $       7           V   $    ^���   
 �   R   T          });�   Q   S            });�   P   R              });�   O   Q          D      admin.firestore().collection(collectionName).doc(id).delete();�   N   P          	      });�   M   O                  imageUrl: downloadUrl1,�   L   N                  videoUrl: downloadUrl1,�   K   M          $      assert.deepEqual(doc.data(), {�   J   L                console.log(doc.data());�   I   K                  .get();�   H   J                  .doc(id)�   G   I          #        .collection(collectionName)�   F   H                  .firestore()�   E   G                const doc = await admin�   D   F          %      const id = await wrapped(snap);�   C   E          	      });�   B   D          	        }�   A   C                     shareLink: shareLink1,�   @   B          !          ownerName: "chelstres",�   ?   A          )          ownerId: "6704092046275642374",�   >   @          )          videoId: "6792361683743526150",�   =   ?          P          firebaseStorageDownloadTokens: "8594eca6-9a01-4385-8a20-f4acc2cf414b",�   <   >          $          downloadUrl: downloadUrl1,�   ;   =                  metadata: {�   :   <          !        contentType: "image/png",�   9   ;          -        bucket: "funfunfun-test.appspot.com",�   8   :          .        name: `images/thumbnails/${videoId1}`,�   7   9          
        },�   6   8                     shareLink: shareLink1,�   5   7          !          ownerName: "chelstres",�   4   6          )          ownerId: "6704092046275642374",�   3   5          )          videoId: "6792361683743526150",�   2   4          P          firebaseStorageDownloadTokens: "8594eca6-9a01-4385-8a20-f4acc2cf414b",�   1   3          $          downloadUrl: downloadUrl1,�   0   2                  metadata: {�   /   1          !        contentType: "image/png",�   .   0          -        bucket: "funfunfun-test.appspot.com",�   -   /          .        name: `images/thumbnails/${videoId1}`,�   ,   .          4      const snap = test.storage.makeObjectMetadata({�   +   -          6      const wrapped = test.wrap(functions.addToLikes);�   *   ,          T    it("should create a database entry in /likes with a download url", async () => {�   )   +          D  describe("normal behavior of adding a url to likes", function () {�   (   *           �   '   )            });�   &   (              //delete console.log;�   %   '              //reset console�   $   &           �   #   %              test.cleanup();�   "   $            after(async () => {�   !   #           �       "            });�      !          #    //console.log = function () {};�                     //silence the console�                 �                �      "https://firebasestorage.googleapis.com/v0/b/funfunfun-25991.appspot.com/o/6792361683743526150.mp4?alt=media&token=8594eca6-9a01-4385-8a20-f4acc2cf414b";�                    downloadUrl1 =�                )    videoId1 = "6792361683743526150.mp4";�                1    shareLink1 = "https://vm.tiktok.com/3awDGF/";�                    collectionName = "likes";�                (    functions = require("../lib/index");�                  before(async () => {�                 �                  let collectionName;�                  let downloadUrl;�                  let videoId1;�                  let shareLink1;�                  let functions;�                  this.timeout(20000);�                $describe("addToLikes", function () {�                 �                9const tiktok = require("../lib/utils/tiktok_scraper.js");�                (const admin = require("firebase-admin");�   
             );�   	             !  "/tmp/serviceAccount-test.json"�      
            },�      	               projectId: "funfunfun-test",�                0    storageBucket: "funfunfun-test.appspot.com",�                9    databaseURL: "https://funfunfun-test.firebaseio.com",�                  {�                0const test = require("firebase-functions-test")(�                2//const functions = require('firebase-functions');�                 �                 !const assert = require("assert");5�_�                    ;       ����                                                                                                                                                                                                                                                                                                                            .   $       7           V   $    ^���     �   :   <   S      !        contentType: "image/png",5�_�                    ;       ����                                                                                                                                                                                                                                                                                                                            .   $       7           V   $    ^���     �   :   <   S      !        contentType: "video/png",5�_�                    9       ����                                                                                                                                                                                                                                                                                                                            .   $       7           V   $    ^���    �   8   :   S      .        name: `images/thumbnails/${videoId1}`,5�_�                    9        ����                                                                                                                                                                                                                                                                                                                            9          C   
       V       ^��     �   8   9          .        name: `videos/thumbnails/${videoId1}`,   -        bucket: "funfunfun-test.appspot.com",   !        contentType: "video/mp4",           metadata: {   $          downloadUrl: downloadUrl1,   P          firebaseStorageDownloadTokens: "8594eca6-9a01-4385-8a20-f4acc2cf414b",   )          videoId: "6792361683743526150",   )          ownerId: "6704092046275642374",   !          ownerName: "chelstres",              shareLink: shareLink1,   
        },5�_�                    -       ����                                                                                                                                                                                                                                                                                                                            9          9   
       V       ^��     �   .   :   I    �   .   /   I    �   -   /   H    5�_�                    .        ����                                                                                                                                                                                                                                                                                                                            E          E   
       V       ^��    �   -   .           5�_�                    '       ����                                                                                                                                                                                                                                                                                                                                                             ^�ݱ     �   &   (   S          //delete console.log;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^�ݳ     �      !   S      #    //console.log = function () {};5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^�ݴ    �      !   S      "    /console.log = function () {};5�_�                   ,        ����                                                                                                                                                                                                                                                                                                                            ,           K           V        ^��n     �   +   ,           6      const wrapped = test.wrap(functions.addToLikes);   4      const snap = test.storage.makeObjectMetadata({   .        name: `videos/thumbnails/${videoId1}`,   -        bucket: "funfunfun-test.appspot.com",   !        contentType: "video/mp4",           metadata: {   $          downloadUrl: downloadUrl1,   P          firebaseStorageDownloadTokens: "8594eca6-9a01-4385-8a20-f4acc2cf414b",   )          videoId: "6792361683743526150",   )          ownerId: "6704092046275642374",   !          ownerName: "chelstres",              shareLink: shareLink1,   
        },   .        name: `images/thumbnails/${videoId1}`,   -        bucket: "funfunfun-test.appspot.com",   !        contentType: "image/png",           metadata: {   $          downloadUrl: downloadUrl1,   P          firebaseStorageDownloadTokens: "8594eca6-9a01-4385-8a20-f4acc2cf414b",   )          videoId: "6792361683743526150",   )          ownerId: "6704092046275642374",   !          ownerName: "chelstres",              shareLink: shareLink1,   
        },   	      });   %      const id = await wrapped(snap);         const doc = await admin           .firestore()   #        .collection(collectionName)           .doc(id)           .get();         console.log(doc.data());5�_�                    0       ����                                                                                                                                                                                                                                                                                                                            ,           ,           V        ^��p     �   /   0          D      admin.firestore().collection(collectionName).doc(id).delete();5�_�                    ,        ����                                                                                                                                                                                                                                                                                                                            ,          /   	       V       ^��w    �   +   ,          $      assert.deepEqual(doc.data(), {           videoUrl: downloadUrl1,           imageUrl: downloadUrl1,   	      });5�_�                     .        ����                                                                                                                                                                                                                                                                                                                            ,          ,   	       V       ^��y    �   ,   .            });�   +   -              });�   *   ,          T    it("should create a database entry in /likes with a download url", async () => {�   )   +          D  describe("normal behavior of adding a url to likes", function () {�   (   *           �   '   )            });�   &   (              delete console.log;�   %   '              //reset console�   $   &           �   #   %              test.cleanup();�   "   $            after(async () => {�   !   #           �       "            });�      !          !    console.log = function () {};�                     //silence the console�                 �                �      "https://firebasestorage.googleapis.com/v0/b/funfunfun-25991.appspot.com/o/6792361683743526150.mp4?alt=media&token=8594eca6-9a01-4385-8a20-f4acc2cf414b";�                    downloadUrl1 =�                )    videoId1 = "6792361683743526150.mp4";�                1    shareLink1 = "https://vm.tiktok.com/3awDGF/";�                    collectionName = "likes";�                (    functions = require("../lib/index");�                  before(async () => {�                 �                  let collectionName;�                  let downloadUrl;�                  let videoId1;�                  let shareLink1;�                  let functions;�                  this.timeout(20000);�                $describe("addToLikes", function () {�                 �                9const tiktok = require("../lib/utils/tiktok_scraper.js");�                (const admin = require("firebase-admin");�   
             );�   	             !  "/tmp/serviceAccount-test.json"�      
            },�      	               projectId: "funfunfun-test",�                0    storageBucket: "funfunfun-test.appspot.com",�                9    databaseURL: "https://funfunfun-test.firebaseio.com",�                  {�                0const test = require("firebase-functions-test")(�                2//const functions = require('firebase-functions');�                 �                 !const assert = require("assert");�   -   .          });5�_�                    ,        ����                                                                                                                                                                                                                                                                                                                            ,          ,           V        ^��i     �   +   Q        5��