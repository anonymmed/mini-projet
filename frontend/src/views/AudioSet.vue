<template>
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-12 main-bar">
          <h4>MANAGE AUDIO SETS</h4>
            </div>
        </div>


        <div class="row">
            <div class="col-lg-4"  style="margin-bottom: 20px;" v-for="audioSet in audioSets">

  <v-card
    class="mx-auto"
    max-width="400"
  >

    <v-img v-if="audioSet.url.indexOf('=')"
      class="white--text align-end"
      height="200px"
      :src="'https://img.youtube.com/vi/' + getVideoId(audioSet.url) + '/0.jpg'"
    >
      <v-card-title>{{audioSet.name}}</v-card-title>
    </v-img>
    <v-img v-else
      class="white--text align-end"
      height="200px"
      src="https://img.youtube.com/vi/' + getVideoId(audioSet.url) + '/0.jpg'"
    >
      <v-card-title>{{audioSet.name}}</v-card-title>
    </v-img>

    <p class="pb-0"></p>

    <v-card-text class="text--primary">
      <div>
      <p v-if="audioSet.transcribed">Transcribed: True</p>
        <p v-else>Transcribed: Flase</p>
      </div>

      <div>Details: {{audioSet.details ? audioSet.details : 'N/A'}}</div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="orange"
        text
        v-on:click="viewAudio(audioSet)"
      >
        View
      </v-btn>

      <v-btn
        color="orange"
        text
        v-on:click="deleteAudio(audioSet)"
      >
        Delete
      </v-btn>
    </v-card-actions>
  </v-card>
            </div>
        </div>
      <br>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "AudioSet",
        data: () => ({
            audioSets: [],
            audioSetUrl: ""
        }),
        methods: {
          getVideoId: function(url) {
                        return url.slice(32,43);
          },
          viewAudio : function (audio) {
                      localStorage.setItem('audioID', audio.id);
                      localStorage.setItem('audioName', audio.name);
                      localStorage.setItem('audioTranscribed', audio.transcribed);
                      localStorage.setItem('audioTranscription', audio.transcription);
                      localStorage.setItem('audioDetails', audio.details);
                      localStorage.setItem('audioAnnotator', audio.annotator);
                      localStorage.setItem('audioUrl', audio.url);
                      localStorage.setItem('audioTags', audio.tags);
                      localStorage.setItem('videoId', this.getVideoId(audio.url));
                      this.$router.push({path: '/view-audio'});

          },
          deleteAudio: function (audio) {

            axios.delete('http://localhost:8080/api/Audios/'+audio.id, {
                    headers: {
                        'Authorization': 'token '+ localStorage.getItem('token'),
                        'Access-Control-Allow-Origin' : '*'
                    }
                }).then((res) => {
                  if (res.status === 204) {
                    let offset = this.audioSets.indexOf(audio);
                    this.audioSets.splice(offset, 1);
                    this.$swal({type: 'success', title: 'AudioSet Has been Deleted', text: 'AudioSet Has been Deleted Successfully!', footer: '<a href="https://batvoice.com">BATVOICE</a>'});
                  }
            }).catch((err) => {
              throw err;
            })
          },
        },
        mounted() {
            axios.get('http://localhost:8080/api/Audios/',
                {
                    headers: {
                        'Authorization': 'token '+ localStorage.getItem('token'),
                        'Access-Control-Allow-Origin' : '*'
                    }
                }
            ).then((res) => {
                if (res.request.status === 200) {
                    this.audioSets = res.data;
                } else {
                    this.$swal({type: 'warning', title: 'Something Wrong Happened', text: 'Please try again!', footer: '<a href="https://batvoice.com">BATVOICE</a>'});
                }
            }).catch((err) => {
                if (err) {
                  throw err;
                }
            });
        },
    }
</script>
<style lang="css">
    @font-face {
  font-family: 'industry';
  src:  url('../styles/fonts/Industry-Bold.woff') format('woff'),
        url('../styles/fonts/Industry-Bold.eot') format('eot');
  font-weight: bold;
  font-style: normal;
}

    .main-bar {
        height: 60px;
        background-color: #0d47a1;
        color: white;
        text-align: center;
        padding: auto;
        margin-bottom: 30px;
    }
    h4{
        font-family: "industry",sans-serif !important;
        padding-top: 0.5%;
    }
</style>