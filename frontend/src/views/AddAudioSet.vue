<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12 main-bar">
                <h4>ADD AN AUDIO SET</h4>
            </div>
        </div>

        <div class="row">
            <div class="col-lg-12 ">
      <v-flex
        xs12
        md12
      >
        <material-card
          color="green"
          title="Audio Description"
          text="Complete the audio data"
        >
          <v-form>
            <v-container py-0>
              <v-layout wrap>
                <v-flex
                  xs12
                  md4
                >

                </v-flex>
                <v-flex
                  xs12
                  md12
                >
                  <v-text-field
                    class="purple-input"
                    label="Audio Name"
                    v-model="name"
                  />
                </v-flex>


                 <v-flex
                                  xs12
                                  md12
                                >
                  <v-text-field
                    class="green-input"
                    label="Audio URL"
                    v-model="url"
                  />
                </v-flex>
                  <v-flex
                  xs12
                  md12
                >
                  <v-textarea
                    class="purple-input"
                    label="Audio Details"
                    v-model="details"
                  />
                </v-flex>

                <v-flex
                  xs12
                  md12
                >
                    <vue-tags-input
                     class="green-input"
                      v-model="tag"
                      :tags="tags"
                      @tags-changed="newTags => tags = newTags"
                    />
                </v-flex>

                <v-flex
                  xs12
                  text-xs-right
                >
                  <v-btn
                    class="mx-0 font-weight-light"
                    color="success" v-on:click="submit"
                  >
                    Add Audio Set
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </material-card>
      </v-flex>
      <v-flex
        xs12
        md4
      >
      </v-flex>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import VueTagsInput from '@johmun/vue-tags-input';

    export default {
        components: {
          VueTagsInput,
        },
        name: "AddAudioSet",
        data: () => ({
            name: "",
            details :"",
            url: "",
            tag: '',
            tags: [],

        }),
        methods : {
            checkUrl : function() {
                var urlPattern = new RegExp("^(http:\\/\\/www\\.|https:\\/\\/www\\.|http:\\/\\/|https:\\/\\/)?[a-z0-9]" +
                    "+([\\-\\.]{1}[a-z0-9]+)*\\.[a-z]{2,5}(:[0-9]{1,5})?(\\/.*)?$");
                if (urlPattern.exec(this.url)) {
                    return true;
                }
                return false;
            },
            submit : function() {
                let Tags ="";
                this.tags.map((t) => {Tags+=t.text+ ', ';});

                if (!this.checkUrl()) {
                    this.$swal({type: 'error', title: 'Oops...', text: 'Please enter a correct AudioSet URL!', footer: '<a href="https://batvoice.com">BATVOICE</a>'});
                    return false;
                } else {
                    axios.post('http://localhost:8080/api/Audios/',
                        {
                            "name": this.name,
                            "transcription": "",
                            "annotator": null,
                            "transcribed": false,
                            "details": this.details,
                            "tags": Tags,
                            "url": this.url
                        },
                        {
                            headers: {
                                'Authorization': 'token '+ localStorage.getItem('token'),
                                'Access-Control-Allow-Origin' : '*'
                            }
                        }
                    ).then((res) => {
                        if (res.request.status === 201) {
                    this.$swal({type: 'success', title: 'Thank you', text: 'AudioSet Added Successfully!', footer: '<a href="https://batvoice.com">BATVOICE</a>'});
                        } else {
                    this.$swal({type: 'warning', title: 'Something Wrong Happened', text: 'Please check the info and try again!', footer: '<a href="https://batvoice.com">BATVOICE</a>'});
                        }
                    }).catch((err) => {
                       if (err) {
                           console.log(err.toString());
                       }
                    });
                return true;
                }

            }
        },
        mounted() {
            console.log("mounted");
        },beforeCreate() {
      if (localStorage.getItem('token')) {
      }else {
          this.$router.push('Login');
      }
  }
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
        margin-bottom: 30px;
        padding: auto;
    }
    h4{
        font-family: "industry",sans-serif !important;
        padding-top: 0.5%;
    }
</style>