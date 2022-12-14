# 입자 모형 시뮬레이션

<strong>오비탈모형 구현 모습</strong>

![orbital](https://github.com/yoonhero/quantum_simulation/blob/master/orbital.gif?raw=true)

<strong>러더포드모형 구현 모습</strong>

![rutherford](https://github.com/yoonhero/quantum_simulation/blob/master/docs/rutherford.png?raw=true)

## 역사

1808년 돌턴은 원자를 더 이상 쪼갤 수 없는 입자의 최소 단위로 하는 원자론을 발표한다. 하지만 이후 톰슨이 음극선관 실험을 통해 전자의 존재를 알아냈다. 그는 원자가 양전하 구름에 음전하를 띤 전자들이 무질서하게 박혀있는 건포도 푸딩모형일 것이라 제안하였다. 1911년, 영국의 과학자 러더퍼드는 톰슨의 원자모형을 입증하기 위한 실험을 했으나 예상과 다른 결과를 얻게 된다. 그는 실험을 통해 원자핵의 존재를 알아내게 된다.

과학계는 톰슨과 러더퍼드 이후 본격적으로 전자와 원자핵에 대한 개념을 만든다. 1913년, 덴마크의 물리학자 닐스 보어는 수소의 선스펙트럼 실험을 통해 수소 원자 내의 전자는 특정한 파장의 에너지만을 방출, 흡수한다는 사실을 알아내었고 양자화한 모형을 주장하여싿. 보어는 전자가 허용된 궤도만을 돈다고 가정하였고 전자를 고전적인 입자로 취급하여 전자의 궤도를 계산했다. 그러나 보어의 모형은 전자가 왜 그러한 거동을 하는지를 전혀 설명하지 못했고, 수소꼴 이외의 원자들은 다른 전자의 가리움 효과로 인한 3체 이상의 문제가 되어 해결하기가 힘들어진다.

1920년에 들어서면서 보어의 원자모형은 타당성을 잃어 원자모형에 대한 전혀 새로운 접근 방법이 시도되었다. 드 브로이, 슈뢰딩거, 하이젠베르크 등의 과학자들은 원자모형을 이해하는 데에 파동 혹은 행렬의 개념을 도입하였다.

드 브로이는 전자가 파동과 입자의 성질을 모두 지녔다는 물질파 이론을 개념화하였다. 슈뢰딩거는 전자가 파동의 성질을 지녔다는 개념을 바탕으로 전자가 핵을 중심으로 정상파와 유사하게 행동한 것으로 보고, 전자를 파동으로 기술하였다. 이를 실험한 결과, 전자는 파장의 정수배에 해당하는 에너지만을 가지고 있었으며 이는 수소원자가 양자화 상태임을 보여줬고 슈뢰딩거는 이를 바탕으로 전자가 정상파처럼 행동한다고 확신해 양자화 된 수소원자를 설명하는 모형을 고안해냈다.

## 오비탈

오비탈은 원자에 귀속된 전자 1개에 대한 파동함수를 의미한다. 이를 엄밀하게 계산해 낼 수 있는 계는 상당히 적지만 다전자 계에서도 전체 계를 1전자 함수들의 곱으로 근사하는 경우 그 때 사용하는 단일 전자의 파동함수 또는 오비탈이라고 부른다.

전자의 파동함수는 복소수가 포함된 꼴로 나타나는데, 파동함수 자체는 아무런 물리적 의미가 없으나 이 파동함수를 제곱하면 특정 위치에서의 전자의 확률 밀도를 얻을 수 있다. 이를 기하적으로 표현할 때는 함수의 등위면을 통해 표현한다.

<strong>파동함수</strong>

$R_{nl}(r) = \sqrt{\Big(\frac{2}{n a_0}\Big)^3 \frac{(n-l-1)!}{2n (n+l)!}} e^{-r/n a_0} \Big( \frac{2r}{na_0}\Big)^l  \cdot L^{2l+1}_{n-l-1} \Big(\frac{2r}{n a_0} \Big)$

![wave_function](https://dpotoyan.github.io/Chem324/images/H-atom-wavef_11_0.png)

-   양자수

    슈뢰딩거 방정식을 푸는 과정에서 파동함수를 결정하기 위해 필요한 값들이다. 이때 양자수의 값들은 이전에 주어지는 것이 아니라, 해를 구하는 과정에서 나오게 된다.

    -   주양자수

        n으로 나타낸다. 자연수의 값만 가질 수 있다. 오비탈의 크기와 에너지 준위를 결정하는 양자수이다. 또한 부양자수를 결정해주는 역할을 한다.

        (즉, 1s오비탈의 경우 주양자수 n=1n=1이다.)

    -   방위 양자수 (부양자수, 각운동량 양자수)

        l로 나타낸다. 0에서 n-1n−1까지의 정수 값을 갖는다. 각운동량(angular momentum)의 크기를 결정하는 양자수이므로 각운동량 양자수라고 한다. 또는 주양자수라는 용어와 세트로 부양자수라고 하기도 한다.

        방위 양자수는 오비탈의 3차원적인 모양을 결정한다.
        예를 들면, s오비탈은 l=0, p오비탈은 l=1, d오비탈은 l=2, f오비탈은 l=3이다.

        수소 원자에서는 방위 양자수는 오비탈의 에너지 준위에 영향을 미치지 않으나, 다전자 원자에서는 방위 양자수도 오비탈의 에너지 준위를 결정한다.

        -   각운동량

            각운동량(L)은 중심을 중심으로 얼마간의 거리를 가지고 회전하는 물체가 가지는 운동량이다.

            ![L](https://mblogthumb-phinf.pstatic.net/MjAxODExMTVfMjM1/MDAxNTQyMjQ0Njg1OTQ1.GsrcZfDQRePDTrkAEzqBDsl39_SfJlKxzV_S56xC94cg.TX81GY5cZ5c75k0Dd3XHi22lmNwq6zjQTirvQHzWhVUg.PNG.falcon2026/image.png?type=w800)

            ![v](https://mblogthumb-phinf.pstatic.net/MjAxODExMTVfMTU3/MDAxNTQyMjQ0NjIwNzg0.RJRUCrCtvkZFZevOOsHkQ4FI59MSRWuqBS3BZ1-wzSMg.m8NvC4m1PWKIfdZho-5JNivQ-nUsK4xFOTTzzxzsDo4g.PNG.falcon2026/image_6221123001542244607021.png?type=w800)

    -   자기 양자수

        m으로 나타낸다. -l−l에서 +l+l까지의 정수 값을 갖는다. 궤도의 방향을 결정하는 양자수이다.

    -   스핀 양자수

        s로 나타낸다. 각운동량과 관련된 전자의 고유 성질이다. 고전적으로는 전자의 자전으로 설명하나 이는 정확하지 못한 설명이다. 왜냐하면 자전으로 얻어지는 각운동량은 무조건 플랑크 상수의 {2n \pi}2nπ (nn은 정수)꼴로 주어져야 하는데, 전자의 스핀은 n=1/2n=1/2로 정수가 아니기 때문이다. 즉 각운동량인데 자전과는 관련이 없는, 양자역학에서 갑툭튀한 개념이라 고전적으론 설명할 수 없다.

-   모양

    ![shape](https://w.namu.la/s/9d311d18f26d38ef01a0cff1e3141840d1c5a76a2545a7cc3b45d9e3fb456816e804d5e9a879d7e45fc5481c9414053896345a8cf53d8264cbfb8b3d2c04737b9bfbc2b36b89b524bc1b8402a92a1f7dccea97689ad99dd685b319e67379cc45)

    각운동량 양자수를 나타내는 s, p, d, f

    -   s-오비탈

        Sharp Orbital

        부양자수가 0인 오비탈을 s-오비탈이라 칭한다. s-오비탈은 구형 대칭이며, 각상의 마디는 갖지 않고, (n-1n−1)개의 방사상 마디를 갖는다.

        주기율표상에서는 수소, 헬륨, 알칼리 금속, 알칼리 토금속의 마지막 전자가 s-오비탈을 띤다.(s-block)

    -   p-오비탈

        Principal Orbital

        부양자수가 1인 오비탈을 p-오비탈이라고 하며, p-오비탈은 핵을 지나는 마디면으로 분리된 두 로브로 이루어진 아령 모양이다.

        주기율표상에서는 붕소족 원소, 탄소족 원소, 질소족 원소, 칼코겐 원소, 할로젠 원소, 비활성 기체의 마지막 전자가 p-오비탈을 띤다.

    -   d-오비탈

        Diffuse Orbital

        부양자수가 2인 오비탈을 d-오비탈이라고 한다. 대체로 네잎클로버와 비슷한 모양을 가지고 있다.

    -   f-오비탈

        Fundamental Orbital

        부양자수가 3인 오비탈을 f-오비탈이라고 한다. f-오비탈의 기하적 형태는 종류에 따라 매우 다르나, 공통적으로 각상 마디가 3개 있다.

    -   g-오비탈

        부양자수가 4인 오비탈을 g-오비탈이라고 한다.

-   혼성 오비탈 모형

    오비탈 이론이 정립되고, 화학자들은 이를 바탕으로 어떻게 원자들이 결합하여 분자를 형성하는지 설명하고 하였다. 가장 직관적인 설명은 원자가 결합 이론(valence bond(VB) theory)이다. VB이론의 기본 원리는 두 원자의 궤도함수가 겹치고 한 쌍의 전자가 그 겹친 영역을 차지 할 때 공유 결합이 형성된다는 것이다.

=> orbital.py 에 구현되어 있습니다!

## 러더퍼드 원자 모형

-   이론적 배경

    -   쿨룽의 법칙

        ![coulomb](https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fssl.pstatic.net%2Fimages.se2%2Fsmedit%2F2013%2F6%2F30%2Fhijz0li5ivlsj4.jpg%22&type=w2)

        같은 종류의 전하 사이에는 척력이 다른 종류의 전하 사이에는 인력이 작용한다.
        두 대전체 사이에 작용하는 전기력 F는 대전체 사이의 거리 r의 제곱에 반비례하고 전하량 q1, q2의 곱에 비례한다.

-   원자 모형

    ![atom](https://github.com/yoonhero/quantum_simulation/blob/master/docs/im1.png?raw=true)

    -   위치 계산법

        ![calcpos](https://github.com/yoonhero/quantum_simulation/blob/master/docs/update_pos_im.png?raw=true)

        가속도를 업데이트 -> 가속도를 적분하여 속도를 업데이트 -> 속도를 적분하여 위치를 알아낸다.

    -   초기값

        ![initial](https://github.com/yoonhero/quantum_simulation/blob/master/docs/initial_im.png?raw=true)

=> rutherford.py 에 구현되어 있습니다!!
