<template>
  <v-app> 
<!--CODEPEN START-->
<div id="app">
    <v-app >
    <main>
      <section>
        <v-parallax src="https://raw.githubusercontent.com/vwxyzjn/vuetify-parallax-starter2/master/src/assets/background3.jpg" height="380">
          <v-layout column align-center justify-center>
            <h2 id="title1" class="display-3"> <strong>Welcome to Doorbell</strong></h2>
            <div id="title1" class="display-1">Your future is at the door.</div>
            <v-btn light v-scroll-to="'#element'" large class="teal lighten-2 white--text" href="https://github.com/vwxyzjn/vuetify-parallax-starter">Get Started</v-btn>
          </v-layout>
        </v-parallax>

        <div id="content">
          <v-layout row wrap class="my-5" >
            <v-flex xs12 sm4>
              <v-card color= "rgba(255, 0, 0, 0)" class="elevation-0">
                <v-card-media height="45px" class="text-xs-center">
                  <v-icon x-large class="brown--text">flash_on</v-icon>
                </v-card-media>
                <v-card-title primary-title>
                  <div class="headline text-xs-center" style="width:100%">Speeds up development</div>
                </v-card-title>
                <v-card-text>
                  We did most of the heavy lifting for you to provide
                  a default stylings that incorporate our custom components.
                  Additionally, we refined animations and transitions to 
                  provide a smoother experience for developers.
                </v-card-text>
              </v-card>
            </v-flex>

            <v-flex xs12 sm4>
              <v-card color= "rgba(255, 0, 0, 0)" class="elevation-0">
                <v-card-media height="45px" class="text-xs-center">
                  <v-icon x-large class="brown--text">group</v-icon>
                </v-card-media>
                <v-card-title primary-title>
                  <div class="headline text-xs-center" style="width:100%">User Experience Focused</div>
                </v-card-title>
                <v-card-text>
                  By utilizing elements and principles of Material Design, 
                  we were able to create a framework that incorporates components
                  and animations that provide more feedback to users. Additionally,
                  a single underlying responsive system across all platforms allow
                  for a more unified user experience.
                </v-card-text>
              </v-card>
            </v-flex>

            <v-flex xs12 sm4>
              <v-card color= "rgba(255, 0, 0, 0)" class="elevation-0">
                <v-card-media height="45px" class="text-xs-center">
                  <v-icon x-large class="brown--text">settings</v-icon>
                </v-card-media>
                <v-card-title primary-title>
                  <div class="headline text-xs-center" style="width:100%">Easy to work with</div>
                </v-card-title>
                <v-card-text>
                  We have provided detailed documentation as well as specific code
                  examples to help new users get started. We are also always open 
                  to feedback and can answer any questions a user may have about 
                  Materialize.
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </div>
      </section>

      <section>
        <v-parallax src="http://360gigapixels.com/assets/images/nyc_side_thumb.png" height="380">
          <v-layout column align-center justify-center>
            
          </v-layout>
        </v-parallax>
      </section>
    </main>
  </v-app>
</div>
<!--CODEPEN END-->

    <!--<div class="containerr">
      <img
        src="./landscape.jpg"
        style = "width:100%"
      ></img>
    </div>
    <h1 class="display-4">Welcome to Doorbell </h1>
    <img class="imageoverlay" align-center src="./assets/Doorbell.png"/>-->

  <div v-if="welcome">
    <!--<v-btn @click="welcome=false">Click this ho </v-btn>-->
  </div>

  <div v-else-if="!welcome">
     <v-container grid-list-md text-xs-center>
            <!--RESUME UPLOAD BEGINS-->
            <div v-for="item in items">
                <div v-if="!item.image">
                  <v-layout column wrap align-center>
                    <v-flex x12 sm3>
                        <h3 id="element" class="display-2">Upload Your Resume Here</h3>
                    </v-flex>
                    <v-flex x12 sm3>
                        <img id="upload" src="./assets/upload_sign.png" />
                    </v-flex>
                    <v-flex x12 sm3>
                        <div class="file-upload">
                        <div class="file-select">
                          <div class="file-select-button" id="fileName">Choose File</div>
                          <div class="file-select-name" id="noFile">No file chosen...</div>                                   
                            <input type="file" name="chooseFile" id="chooseFile" accept=".docx" @change="onFileChange($event), fileUploaded(item, $event)">
                        </div>
                        </div>
                    </v-flex>
                  </v-layout>
                </div>

                <div v-else>
                  <v-layout column>
                      <v-flex x12 sm3>
                      <img id="displayedPic" :src="item.image" />
                      </v-flex>
                      <v-flex x12 sm3>
                      <v-btn color="primary" @click="removeImage(item),emitGlobalClickEvent()">Choose Another Image</v-btn>
                      </v-flex>
                  </v-layout>
                </div>
            </div>                      
            <!--RESUME UPLOAD ENDS-->

        </v-container>
    </div>
    </body>
  </v-app>
</template>

<script>
import { upload } from './file-upload.service';
import * as axios from 'axios';

export default {
    name: 'app',
    data() {
      return {
        uploadedFiles: [],
        uploadError: null,
        currentStatus: null,
        uploadFieldName: 'photos',
        items: [
         {
           image: false,
         },
        ],
        welcome: false,
        label:"click here to push meera's buttons",
      }
    },


    methods: {
    fileUploaded(item, e) {
      this.imageChosen = true;
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(item, files[0]);
    },
    reset(){

    },
    onFileChange(event){
        let data = new FormData();
        let file = event.target.files[0];

        data.append('name', 'my-file')
        data.append('file', file)
        let config = {
          header : {
           'Content-Type' : 'multipart/form-data'
         }
        }
        upload(data)

    }
    },

      toggleLable() {
      if (this.label == "click here to push meera's buttons") {
        this.label = "Meera's buttons are pushed, oh boi";
      } else {
        this.label = "click here to push meera's buttons";
      }
    },
    
};

</script>

<style>
.containerr {
  position: relative;
  text-align: center;
}
.display-4 {
  position: absolute;
  top: 15%;
  left:15%;
}
.imageoverlay {
  position: absolute;
  height: 200px;
  top:25%;
  left:39%;
}
#upload{
  height:70px;
}
.file-upload{display:block;text-align:center;font-family: Helvetica, Arial, sans-serif;font-size: 12px;}
.file-upload .file-select{display:block;border: 2px solid #dce4ec;color: #34495e;cursor:pointer;height:40px;line-height:40px;text-align:left;background:#FFFFFF;overflow:hidden;position:relative;}
.file-upload .file-select .file-select-button{background:#dce4ec;padding:0 10px;display:inline-block;height:40px;line-height:40px;}
.file-upload .file-select .file-select-name{line-height:40px;display:inline-block;padding:0 10px;}
.file-upload .file-select:hover{border-color:#34495e;transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;}
.file-upload .file-select:hover .file-select-button{background:#34495e;color:#FFFFFF;transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;}
.file-upload.active .file-select{border-color:#3fa46a;transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;}
.file-upload.active .file-select .file-select-button{background:#3fa46a;color:#FFFFFF;transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;}
.file-upload .file-select input[type=file]{z-index:100;cursor:pointer;position:absolute;height:100%;width:100%;top:0;left:0;opacity:0;filter:alpha(opacity=0);}
.file-upload .file-select.file-select-disabled{opacity:0.65;}
.file-upload .file-select.file-select-disabled:hover{cursor:default;display:block;border: 2px solid #dce4ec;color: #34495e;cursor:pointer;height:40px;line-height:40px;margin-top:5px;text-align:left;background:#FFFFFF;overflow:hidden;position:relative;}
.file-upload .file-select.file-select-disabled:hover .file-select-button{background:#dce4ec;color:#666666;padding:0 10px;display:inline-block;height:40px;line-height:40px;}
.file-upload .file-select.file-select-disabled:hover .file-select-name{line-height:40px;display:inline-block;padding:0 10px;}

@media (min-width: 800px) {
  .toolbar__title {
    margin-left: 15%;
  }
  #content {
    width: 70%;
    margin: auto;
  }
  #footer-layout {
    width:70%!important;
    margin:auto;
  }
}

#footer-layout {
  width: 100%;
}

#subtitle {
  font-weight: 200!important;
}


#footer {
  overflow: auto;
}
.card {
  background-color: #fafafa!important;
}
footer {
  overflow: auto;
}
a {
  color: #fff;

}
#title1 {
    color: rgb(
250,108,122);

}
</style>
