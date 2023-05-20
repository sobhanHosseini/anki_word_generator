def front():
    return '''
        <div id="rubric">TPO Words</div>

        <br><br><br>
        <div style='font-size: 10px'>
        <br><br><br><br><br></div>

        <div style='font-family: Comic Sans MS ; font-size: 50px; text-align: center; color: crimson '> {{Word}}</div>

        <div style='font-size: 10px'>
        <br><br></div>

        <div style='text-align: center; '> [sound:{{Word}}.mp3]</div>

        <div style='font-size: 10px'>
        <br><br></div>

        <div style='font-family: times new roman ; text-align: center; font-size: 35px; color: orangered '>{{Phonetic}}
        </div><br>
        <div style='font-family: Comic Sans MS; text-align: center; font-size: 30px; color: orangered '>{{PartOfSpeech}}</div>
        <br><br>
        '''
    
def back():
    return style() + '''
                <div style='font-family: Comic Sans MS ; text-align: center; font-size: 25px; color: orangered '> <b>{{Word}}</b>[sound:{{Word}}.mp3] {{Phonetic}}</div>

                <!hr id=answer>
                <div class="mini_space"><hr><div></div>
                <div class="title">
                <b>Definition</b></div>
                <hr>
                <div class="mini_space"><br></div>
                <div style='font-family: Comic Sans MS; font-size: 18px; color: #aa007f '>{{Definition}}</div>
                <div><br>

                <div class="mini_space"><hr></div>

                {{#Synonyms}}
                <div class="title">
                <b>Synonyms</b></div>
                <hr>
                <div class="mini_space"><br></div>
                <div style="font-family: Comic Sans MS; text-align: center; font-size: 19px; color: darkblue ">{{Synonyms}}

                <span style='font-family: Comic Sans MS; text-align: center; font-size: 19px; color: steelblue '>[sound:{{Synonyms}}.mp3]
                </span></div>
                <div>
                {{/Synonyms}}
                


                {{#Examples}}
                <div class="mini_space"><hr></div>
                <div class="title">
                <b>Examples</b></div><hr>

                <div class="frontbg_top">

                <div style='font-family: Comic Sans MS ; text-align: justify; margin-left: 3%; margin-right: 3%; margin-top: 1%; margin-bottom: 2%; font-size: 17px; color: #00557f '>{{Examples}}</div></div>
                {{/Examples}}
                <br>

                <br><br><br><br><br><br>
                <br><br><br><br><br><br>
                '''
        
def style():
    return '''
        <style>
            .card {
        font-family: Comic Sans MS;
        font-size: 22px;
        color: black;
        background-color: white;
        text-align: center;
        background-attachment: fixed;
        background-size: auto 100%;
        background-position: center;
        background-repeat: repeat;
        }


        @font-face { 
        font-family: Comic Sans MS;
        src: url('_comic.ttf');
        }


        .farsi{
        color: #f9f4f0;
        font-family: XB zar;
        font-size: 4px;
        direction: rtl;
        text-align: center;
        }

        .farsi:hover{
        color: #aa007f;
        font-family: XB zar;
        font-size: 16px;
        direction: rtl;
        text-align: center;
        }




        img {
        Width: 300px;
        height: 170px;
        border-radius: 15px;
        }

        #rubric {
        text-align: center;
        font-family: arial;
        padding: 3px;
        padding-left: 10px;
        padding-right: 10px;
        margin-bottom: 10px;
        background: orangered;
        color: black;
        font-weight: 500;
        }

        .title{
        font-family:times new roman;
        text-align: center;
        font-size: 17px;
        background-color: #FFFF99;
        color: teal;
        border-radius: 12px 12px 12px 12px;
        }

        .notice{
        text-align:left;
        font-family: times new roman;
        font-size: 19px;
        color: orangered;
        margin-left: 3%;
        margin-right: 3%;
        margin-top: 1%;
        margin-bottom: 1%;
        }



        .mini_space{
        font-size: 3px;
        text-align: center;
        }




        .frontbg_top {
            background-color: white;
            border-radius: 0 0 12px 12px;
            color: #fff;
            padding: 1.5em 0 0.5em 0;
        }

        .frontbg_bottom {
            background-color: rgba(84, 143, 141, 0.45);
            border-radius: 0 0 12px 12px;
            color: #fff;
            padding: 1em 1em 1.5em 1em;
        }
        .expression {
            font-size: 30pt;
        }

        .reading {
            font-size: 12pt;
        }

        .sentence {
            font-size: 13pt;
        text-align: left;
        color: #ddd;
        }

        .reading + .sentence {
            padding-top: 1em;
        }

        .cloze_highlight {
            color: #fff;
            font-weight: bold;
        }

        .frontbg_top .meaning {
            font-size: 18pt;
        }

        .meaning {
            padding: 1em;
        }
    </style>
    '''
    