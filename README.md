# Python-Team-Project
2020년 2학기 2D게임프로그래밍 과제 제출용 프로젝트입니다.

## 1.	게임의 소개

- 제목


      동방과제록
    
- Copy 게임이라면, 원 게임에 대한 정보 및 스크린 샷
	    
      東方Project / Touhou Project / Project Shrine Maiden라고 불린다. 제작자 이름은 ZUN, 
      
      1인 동인서클인 상하이앨리스환악단에서 만든 동인 게임 시리즈로, 원작 장르는 블록 격파 게임과 탄막 슈팅 게임이다.
      
      
     ![동방 프로젝트 게임](https://user-images.githubusercontent.com/27701868/94260060-756e4a80-ff6a-11ea-9ac4-6052f87450d5.jpg)
      
     <01. 동방 프로젝트 게임의 플레이 장면>

- 게임의 목적, 방법 등 간단한 설명

      게임의 목적  
      
         내려오는 적들의 공격을 피하고 플레이어에게서 발사되는 총알을 맞춰 점수를 높게 올리는 것이 목적이다.

      게임의 방법  
      
         wasd키나 방향키로 캐릭터를 움직이고, spacebar를 눌러 총알을 발사하여 적대적 오브젝트를 파괴하고 점수를 얻는다.


## 2.	GameState(Scene)의 수 및 각각의 이름
    
       6개, LogoState, TitleState, OptionState, ManualState, GameState, ScoreState



## 3.	각 GameState(Scene) 별 다음 항목


-	1. LogoState
       1. 게임에 관련된 장면 몇 개를 보여준다.
       2. Change -> TitleStat  
       
       
-	2. TitleState
       1. 게임 시작, 옵션 설정, 매뉴얼, 나가기 4가지로 이루어져 있다. 각 버튼은 spacebar와 방향키 버튼으로 눌러 해당 state로 이동한다.
       2. Push -> GameState | Push -> OptionState | Push -> ManualState | Pop -> Quit


-	3. OptionState
       1. spacebar와 방향키 버튼으로 음성 지원 유무와 애니메이션 출력 여부를 선택한다.
       2. Pop -> TitleState or GameState


-	4. ManualState
       1. 게임의 조작법을 설명한다.
       2. Pop -> TitleState


-	5. GameState
       1. 게임을 플레이하는 부분으로 방향키와 spacebar를 사용하여 게임을 진행한다.
       2. 스테이지 별로 나뉘어 있으며, 해당 스테이지가 끝날 때 마다 다음 스테이지로 넘어갈지 게임을 종료할지 결정할 수 있다. (해당 기능은 최종적으로 제거한다.)
       3. 최소 1개의 스테이지가 구성되어 있으며 시간이 되는대로 추가할 계획이다.
       4. Change -> ScoreState | Pop -> TitleState | Push -> OptionState
       5. 객체 : 플레이어, 몬스터, 보스


-	6. ScoreState
       1. 게임이 끝난 후 자신의 점수가 기록된 판을 불러온다.
       2. Pop -> TitleState
 
 
 
 
 ![파이썬 기말 프로젝트 간단 설명](https://user-images.githubusercontent.com/27701868/94259859-1c061b80-ff6a-11ea-96bc-4d3775052547.png)

<02. 다이어그램으로 나타낸 State 설계도>



## 4.	필요한 기술
- 다른 과목에서 배운 기술

	  이미지 넣기(+ 경로 설정), 더블 버퍼링, 마우스 및 키 이벤트 처리, 음향 처리

- 이 과목에서 배울 것으로 기대되는 기술

	  프레임 워크에 대한 기본 구조


- 다루지 않는 것 같아서 수업에 다루어 달라고 요청할 기술

      영상 처리 방법, 인 게임에서 영상을 출력하고 싶으면 어떻게 해야 하나요?



