# Python-Team-Project
2020년 2학기 2D게임프로그래밍 과제 제출용 프로젝트입니다.

## 1.	게임의 소개

- 제목


      동방과제록(東方課題錄)
    
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


## 5. 게임의 컨셉

-	적은 위에서 아래로 이동하는데 맵 끝까지 이동하게 되면 사라지는 구조로 이루어져 있습니다.

-	적이 이동하는 동안 플레이어가 적을 공격하면 공격에 맞은 적은 체력이 줄고, 체력이 0이하로 떨어지면 사라지게 됩니다. 

-	이렇게 적을 소멸시키면 점수가 오르게 되는데 최종적인 점수를 높게 받는 것이 이 게임의 목표입니다.




## 6. 게임의 개발범위

![개발 내용](https://user-images.githubusercontent.com/27701868/95699479-7c41d080-0c7f-11eb-9a17-68d42c805706.PNG)



## 6. 게임의 개발일정


![개발 일정](https://user-images.githubusercontent.com/27701868/95699481-7d72fd80-0c7f-11eb-8d78-1652b759234e.PNG)




## 7. main game state에 등장하는 game objecte들의 정보

### 01. class 구성 정보

1. Player	Enemy
2. Bullet	Pattern	Generator
3. Score	Background	Button


### 02. 상호작용 정보
![main game state object class 상호작용 정보](https://user-images.githubusercontent.com/27701868/99965117-c0280980-2dd7-11eb-9dd3-79645dd59685.png)


### 03. 클래스별 핵심 코드에 대한 간단한 설명
![background](https://user-images.githubusercontent.com/27701868/99965534-5825f300-2dd8-11eb-9a6b-b8520a599452.PNG)
![bullet](https://user-images.githubusercontent.com/27701868/99965542-59572000-2dd8-11eb-9a29-2e3ef8cb4645.PNG)
![button](https://user-images.githubusercontent.com/27701868/99965543-59572000-2dd8-11eb-9e36-f236005912f2.PNG)
![enemey](https://user-images.githubusercontent.com/27701868/99965545-59efb680-2dd8-11eb-8c6a-ff77400641af.PNG)
![generator](https://user-images.githubusercontent.com/27701868/99965548-5a884d00-2dd8-11eb-9d0d-ecf01986542c.PNG)
![pattern](https://user-images.githubusercontent.com/27701868/99965550-5a884d00-2dd8-11eb-9128-f489a3202873.PNG)
![player](https://user-images.githubusercontent.com/27701868/99965552-5b20e380-2dd8-11eb-9332-ddabf9ada8ff.PNG)
![score](https://user-images.githubusercontent.com/27701868/99965555-5b20e380-2dd8-11eb-88d4-02867315c98a.PNG)



edit test
