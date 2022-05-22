# sky_music_auto_play
任天堂Switc版「Sky 星を紡ぐ子どもたち」内で楽器を自動演奏したりMIDIキーボードで演奏したりできるプログラムです。
このプログラムはRaspberry Pi 4 Model B上で実行するものです。
環境構築法はプロコントローラー連射パッド化と同じです
https://qiita.com/Bokuchin/items/0d1f81d79ff8058a729c

使い方
Sky Studioで作られたjsonファイルを「json2csv.py」でcsvに変換します。
変換したcsvは最後の音を離すデータが書き込まれないので、手動で書き込みます。
そうしたものが「guresenbon.csv」です。
今回は律皮MerodPさんが作成されたjsonファイルを使わせて頂きました。
https://www.youtube.com/watch?v=mxjfiagOWrU

「skyauto.py」がそのcsvを読み込んで自動演奏をします。
デモ動画
https://www.youtube.com/watch?v=UYEKxlFTqvI
