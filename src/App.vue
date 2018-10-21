<template>
  <v-app>
    <div v-if="!fileHasBeenUploaded">
        <!--CODEPEN START-->
        <div id="app">
            <v-app >
            <main>
              <section>
                <v-parallax src="https://raw.githubusercontent.com/vwxyzjn/vuetify-parallax-starter2/master/src/assets/background3.jpg" height="380">
                  <v-layout column align-center justify-center>
                    <h2 id="title1" class="display-3"> <strong>Welcome to Doorbell</strong></h2>
                    <div id="title1" class="display-1">Your future is at the door.</div>
                    <v-btn light v-scroll-to="'#element'" large color="grey" href="https://github.com/vwxyzjn/vuetify-parallax-starter">Get Started</v-btn>
                  </v-layout>
                </v-parallax>

                <div id="content">
                  <v-layout row wrap class="my-5" >
                    <v-flex xs12 sm4>
                      <v-card color= "rgba(255, 0, 0, 0)" class="elevation-0">
                        <v-card-media height="45px" class="text-xs-center">
                          <v-icon x-large class="teal--text">flash_on</v-icon>
                        </v-card-media>
                        <v-card-title primary-title>
                          <div class="headline text-xs-center" style="width:100%">Accelerate your career</div>
                        </v-card-title>
                        <v-card-text>
                          Our innovative system allows you to drastically change the way people view your professional experience. For many, years or even decades of experience are ultimately summarized by your resume, so why wouldn’t you put your best foot forward? Our system ensures that you get the feedback necessary to bring your professional presentation to the next level, removing any grammatical blemish holding you back and expressing key skills that will take you forward.
                        </v-card-text>
                      </v-card>
                    </v-flex>

                    <v-flex xs12 sm4>
                      <v-card color= "rgba(255, 0, 0, 0)" class="elevation-0">
                        <v-card-media height="45px" class="text-xs-center">
                          <v-icon x-large class="teal--text">group</v-icon>
                        </v-card-media>
                        <v-card-title primary-title>
                          <div class="headline text-xs-center" style="width:100%">Easy to use</div>
                        </v-card-title>
                        <v-card-text>
                          We offer easy-to-use services that maximize the appeal of your resume while minimizing stress for you. No matter your background, the barrier between you and your best resume is only ever a click of a button. We in ensure efficient and straightforward feedback so that you will have have the opportunity to present your professional self how you always imagined. 
                        </v-card-text>
                      </v-card>
                    </v-flex>

                    <v-flex xs12 sm4>
                      <v-card color= "rgba(255, 0, 0, 0)" class="elevation-0">
                        <v-card-media height="45px" class="text-xs-center">
                          <v-icon x-large class="teal--text">settings</v-icon>
                        </v-card-media>
                        <v-card-title primary-title>
                          <div class="headline text-xs-center" style="width:100%">Feature rich</div>
                        </v-card-title>
                        <v-card-text>
                          We offer a rich suite of features, each designed to optimize your return on your resumé. Some of these include grammatical verification and key word suggestion to bypass early-stage automated filtering and catch the eye of a potential employers. We consider every detail, so you don’t have to.
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
        <v-container grid-list-md text-xs-center>
            <!--RESUME UPLOAD BEGINS-->
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
                            <input type="file" name="chooseFile" id="chooseFile" accept=".docx" @change="onFileChange($event)">
                        </div>
                        </div>
                    </v-flex>

                  </v-layout>
            <!--RESUME UPLOAD ENDS-->
        </v-container>
    </body>
    </div>

    <div v-else-if="fileHasBeenUploaded">

      <v-layout row wrap>
      <div>
        
        <v-layout justify-left column wrap>
        <div class="text-md-left">
        <h2>HIGHLIGHT LEGEND:</h2>
        <div>
            <v-chip large color="indigo" text-color="white">
            Capitalization
                <v-icon right>keyboard_capslock</v-icon>
            </v-chip>
            <v-text>The first letter of every sentence should be capitalized</v-text>
          </div>
          
          <div>
            <v-chip color="green" text-color="white">
              Periods
              <v-icon right>scatter_plot</v-icon>
            </v-chip>
            <v-text>Inconsistency amongs period use across sentences</v-text>
          </div>

          <div>
            <v-chip color="pink" text-color="white">
              Spell Check
              <v-icon right>spellcheck</v-icon>
            </v-chip>
            <v-text>Microsoft Azure identified spelling errors</v-text>
          </div>

          <div>
            <v-chip color="yellow" text-color="white">
              Verb Tense
              <v-icon right>access_time</v-icon>
            </v-chip>
            <v-text>Google Cloud Natural Language present tense inconsistencies</v-text>
          </div>
          
        </div>
        <div>
          <v-card width="30%">
            <v-card-title>Relevant Keywords</v-card-title>
            <v-card-text>Based on your perspective field, we've compiled some common keywords that employers in this space look for. These are not currently in your resume, so if you have any relevant experience with these topics consider adding them.</v-card-text>
          </v-card>
        </div>

        </v-layout>
        </div>


        </v-layout>
      <pdf 
        src="https://cdn.mozilla.net/pdfjs/tracemonkey.pdf"
        @num-pages="pageCount = $event"
        @page-loaded="currentPage = $event"
      ></pdf>
    </div>
  </v-app>
</template>

<script>
import { upload } from './file-upload.service';
import pdf from 'vue-pdf'
import * as axios from 'axios';

export default {
    name: 'app',
    components: {
      pdf
    },
    data() {
      return {
        uploadedFiles: [],
        uploadError: null,
        currentStatus: null,
        uploadFieldName: 'photos',
        fileHasBeenUploaded: false,
        currentPage: 0,
        pageCount: 0,
        
      }
    },


    methods: {

    reset(){

    },
    onFileChange(event){
        console.log("onefilechangeran");
        this.fileHasBeenUploaded = true;

       /* let data = new FormData();
        let file = event.target.files[0];

        data.append('name', 'my-file')
        data.append('file', file)
        let config = {
          header : {
           'Content-Type' : 'multipart/form-data'
         }
        }
        upload(data)*/

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
