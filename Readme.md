# K-Means Clustering
Implementation of K-Means Clustering algorithm using python


## Dataset
CIFAR-10, contains 60000 32x32 images, where 50000 are used for training 


To find out more about the dataset: <https://www.cs.toronto.edu/~kriz/cifar.html>


Directory of data-set 
```
/cifar-10-batches-py
```


## How To Run The Progam
1. Run main.py
2. Enter the value of k
3. Enter the number of iterations
4. Wait for the program to complete


## Output
Ouptut of the run is generated in 
```
/output/iterations= xx, k= xx/run_id=x
```
It contains:
1. Centroids and samples from each cluster
2. Distortion measure graph
3. Excel sheet containing accuracy fit data

### Sample Output When K= 10 and Iterations= 30

#### Centroids and Samples From Each Cluster
##### Centroids from Cluster 0
 
 
![](./readme-assets/0/000.png)![](./readme-assets/0/010.png)![](./readme-assets/0/020.png)![](./readme-assets/0/030.png)![](./readme-assets/0/040.png)![](./readme-assets/0/050.png)![](./readme-assets/0/060.png)![](./readme-assets/0/070.png)![](./readme-assets/0/080.png)![](./readme-assets/0/090.png)![](./readme-assets/0/100.png)![](./readme-assets/0/110.png)![](./readme-assets/0/120.png)![](./readme-assets/0/130.png)![](./readme-assets/0/140.png)![](./readme-assets/0/150.png)![](./readme-assets/0/160.png)![](./readme-assets/0/170.png)![](./readme-assets/0/180.png)![](./readme-assets/0/190.png)![](./readme-assets/0/200.png)![](./readme-assets/0/210.png)![](./readme-assets/0/220.png)![](./readme-assets/0/230.png)![](./readme-assets/0/240.png)![](./readme-assets/0/250.png)![](./readme-assets/0/260.png)![](./readme-assets/0/270.png)![](./readme-assets/0/280.png)![](./readme-assets/0/290.png)![](./readme-assets/0/300.png)
 
 
##### Samples from Cluster 0
 
 
![](./readme-assets/0/310.png)![](./readme-assets/0/311.png)![](./readme-assets/0/312.png)![](./readme-assets/0/313.png)![](./readme-assets/0/314.png)![](./readme-assets/0/315.png)![](./readme-assets/0/316.png)![](./readme-assets/0/317.png)![](./readme-assets/0/318.png)![](./readme-assets/0/319.png)
 
 
##### Centroids from Cluster 1
 
 
![](./readme-assets/1/001.png)![](./readme-assets/1/011.png)![](./readme-assets/1/021.png)![](./readme-assets/1/031.png)![](./readme-assets/1/041.png)![](./readme-assets/1/051.png)![](./readme-assets/1/061.png)![](./readme-assets/1/071.png)![](./readme-assets/1/081.png)![](./readme-assets/1/091.png)![](./readme-assets/1/101.png)![](./readme-assets/1/111.png)![](./readme-assets/1/121.png)![](./readme-assets/1/131.png)![](./readme-assets/1/141.png)![](./readme-assets/1/151.png)![](./readme-assets/1/161.png)![](./readme-assets/1/171.png)![](./readme-assets/1/181.png)![](./readme-assets/1/191.png)![](./readme-assets/1/201.png)![](./readme-assets/1/211.png)![](./readme-assets/1/221.png)![](./readme-assets/1/231.png)![](./readme-assets/1/241.png)![](./readme-assets/1/251.png)![](./readme-assets/1/261.png)![](./readme-assets/1/271.png)![](./readme-assets/1/281.png)![](./readme-assets/1/291.png)![](./readme-assets/1/301.png)
 

##### Samples from Cluster 1
 
 
![](./readme-assets/1/320.png)![](./readme-assets/1/321.png)![](./readme-assets/1/322.png)![](./readme-assets/1/323.png)![](./readme-assets/1/324.png)![](./readme-assets/1/325.png)![](./readme-assets/1/326.png)![](./readme-assets/1/327.png)![](./readme-assets/1/328.png)![](./readme-assets/1/329.png)
 
 
##### Centroids from Cluster 2
 
 
![](./readme-assets/2/002.png)![](./readme-assets/2/012.png)![](./readme-assets/2/022.png)![](./readme-assets/2/032.png)![](./readme-assets/2/042.png)![](./readme-assets/2/052.png)![](./readme-assets/2/062.png)![](./readme-assets/2/072.png)![](./readme-assets/2/082.png)![](./readme-assets/2/092.png)![](./readme-assets/2/102.png)![](./readme-assets/2/112.png)![](./readme-assets/2/122.png)![](./readme-assets/2/132.png)![](./readme-assets/2/142.png)![](./readme-assets/2/152.png)![](./readme-assets/2/162.png)![](./readme-assets/2/172.png)![](./readme-assets/2/182.png)![](./readme-assets/2/192.png)![](./readme-assets/2/202.png)![](./readme-assets/2/212.png)![](./readme-assets/2/222.png)![](./readme-assets/2/232.png)![](./readme-assets/2/242.png)![](./readme-assets/2/252.png)![](./readme-assets/2/262.png)![](./readme-assets/2/272.png)![](./readme-assets/2/282.png)![](./readme-assets/2/292.png)![](./readme-assets/2/302.png)
 
 
##### Samples from Cluster 2
 
 
![](./readme-assets/2/330.png)![](./readme-assets/2/331.png)![](./readme-assets/2/332.png)![](./readme-assets/2/333.png)![](./readme-assets/2/334.png)![](./readme-assets/2/335.png)![](./readme-assets/2/336.png)![](./readme-assets/2/337.png)![](./readme-assets/2/338.png)![](./readme-assets/2/339.png)
 
 
##### Centroids from Cluster 3
 
 
![](./readme-assets/3/003.png)![](./readme-assets/3/013.png)![](./readme-assets/3/023.png)![](./readme-assets/3/033.png)![](./readme-assets/3/043.png)![](./readme-assets/3/053.png)![](./readme-assets/3/063.png)![](./readme-assets/3/073.png)![](./readme-assets/3/083.png)![](./readme-assets/3/093.png)![](./readme-assets/3/103.png)![](./readme-assets/3/113.png)![](./readme-assets/3/123.png)![](./readme-assets/3/133.png)![](./readme-assets/3/143.png)![](./readme-assets/3/153.png)![](./readme-assets/3/163.png)![](./readme-assets/3/173.png)![](./readme-assets/3/183.png)![](./readme-assets/3/193.png)![](./readme-assets/3/203.png)![](./readme-assets/3/213.png)![](./readme-assets/3/223.png)![](./readme-assets/3/233.png)![](./readme-assets/3/243.png)![](./readme-assets/3/253.png)![](./readme-assets/3/263.png)![](./readme-assets/3/273.png)![](./readme-assets/3/283.png)![](./readme-assets/3/293.png)![](./readme-assets/3/303.png)
 
 
##### Samples from Cluster 3
 
 
![](./readme-assets/3/340.png)![](./readme-assets/3/341.png)![](./readme-assets/3/342.png)![](./readme-assets/3/343.png)![](./readme-assets/3/344.png)![](./readme-assets/3/345.png)![](./readme-assets/3/346.png)![](./readme-assets/3/347.png)![](./readme-assets/3/348.png)![](./readme-assets/3/349.png)
 
 
##### Centroids from Cluster 4
 
 
![](./readme-assets/4/004.png)![](./readme-assets/4/014.png)![](./readme-assets/4/024.png)![](./readme-assets/4/034.png)![](./readme-assets/4/044.png)![](./readme-assets/4/054.png)![](./readme-assets/4/064.png)![](./readme-assets/4/074.png)![](./readme-assets/4/084.png)![](./readme-assets/4/094.png)![](./readme-assets/4/104.png)![](./readme-assets/4/114.png)![](./readme-assets/4/124.png)![](./readme-assets/4/134.png)![](./readme-assets/4/144.png)![](./readme-assets/4/154.png)![](./readme-assets/4/164.png)![](./readme-assets/4/174.png)![](./readme-assets/4/184.png)![](./readme-assets/4/194.png)![](./readme-assets/4/204.png)![](./readme-assets/4/214.png)![](./readme-assets/4/224.png)![](./readme-assets/4/234.png)![](./readme-assets/4/244.png)![](./readme-assets/4/254.png)![](./readme-assets/4/264.png)![](./readme-assets/4/274.png)![](./readme-assets/4/284.png)![](./readme-assets/4/294.png)![](./readme-assets/4/304.png)
 
 
##### Samples from Cluster 4
 
 
![](./readme-assets/4/350.png)![](./readme-assets/4/351.png)![](./readme-assets/4/352.png)![](./readme-assets/4/353.png)![](./readme-assets/4/354.png)![](./readme-assets/4/355.png)![](./readme-assets/4/356.png)![](./readme-assets/4/357.png)![](./readme-assets/4/358.png)![](./readme-assets/4/359.png)
 
 
##### Centroids from Cluster 5
 
 
![](./readme-assets/5/005.png)![](./readme-assets/5/015.png)![](./readme-assets/5/025.png)![](./readme-assets/5/035.png)![](./readme-assets/5/045.png)![](./readme-assets/5/055.png)![](./readme-assets/5/065.png)![](./readme-assets/5/075.png)![](./readme-assets/5/085.png)![](./readme-assets/5/095.png)![](./readme-assets/5/105.png)![](./readme-assets/5/115.png)![](./readme-assets/5/125.png)![](./readme-assets/5/135.png)![](./readme-assets/5/145.png)![](./readme-assets/5/155.png)![](./readme-assets/5/165.png)![](./readme-assets/5/175.png)![](./readme-assets/5/185.png)![](./readme-assets/5/195.png)![](./readme-assets/5/205.png)![](./readme-assets/5/215.png)![](./readme-assets/5/225.png)![](./readme-assets/5/235.png)![](./readme-assets/5/245.png)![](./readme-assets/5/255.png)![](./readme-assets/5/265.png)![](./readme-assets/5/275.png)![](./readme-assets/5/285.png)![](./readme-assets/5/295.png)![](./readme-assets/5/305.png)
 
 
##### Samples from Cluster 5
 
 
![](./readme-assets/5/360.png)![](./readme-assets/5/361.png)![](./readme-assets/5/362.png)![](./readme-assets/5/363.png)![](./readme-assets/5/364.png)![](./readme-assets/5/365.png)![](./readme-assets/5/366.png)![](./readme-assets/5/367.png)![](./readme-assets/5/368.png)![](./readme-assets/5/369.png)
 
 
##### Centroids from Cluster 6
 
 
![](./readme-assets/6/006.png)![](./readme-assets/6/016.png)![](./readme-assets/6/026.png)![](./readme-assets/6/036.png)![](./readme-assets/6/046.png)![](./readme-assets/6/056.png)![](./readme-assets/6/066.png)![](./readme-assets/6/076.png)![](./readme-assets/6/086.png)![](./readme-assets/6/096.png)![](./readme-assets/6/106.png)![](./readme-assets/6/116.png)![](./readme-assets/6/126.png)![](./readme-assets/6/136.png)![](./readme-assets/6/146.png)![](./readme-assets/6/156.png)![](./readme-assets/6/166.png)![](./readme-assets/6/176.png)![](./readme-assets/6/186.png)![](./readme-assets/6/196.png)![](./readme-assets/6/206.png)![](./readme-assets/6/216.png)![](./readme-assets/6/226.png)![](./readme-assets/6/236.png)![](./readme-assets/6/246.png)![](./readme-assets/6/256.png)![](./readme-assets/6/266.png)![](./readme-assets/6/276.png)![](./readme-assets/6/286.png)![](./readme-assets/6/296.png)![](./readme-assets/6/306.png)
 
 
##### Samples from Cluster 6
 
 
![](./readme-assets/6/370.png)![](./readme-assets/6/371.png)![](./readme-assets/6/372.png)![](./readme-assets/6/373.png)![](./readme-assets/6/374.png)![](./readme-assets/6/375.png)![](./readme-assets/6/376.png)![](./readme-assets/6/377.png)![](./readme-assets/6/378.png)![](./readme-assets/6/379.png)
 
 
##### Centroids from Cluster 7
 
 
![](./readme-assets/7/007.png)![](./readme-assets/7/017.png)![](./readme-assets/7/027.png)![](./readme-assets/7/037.png)![](./readme-assets/7/047.png)![](./readme-assets/7/057.png)![](./readme-assets/7/067.png)![](./readme-assets/7/077.png)![](./readme-assets/7/087.png)![](./readme-assets/7/097.png)![](./readme-assets/7/107.png)![](./readme-assets/7/117.png)![](./readme-assets/7/127.png)![](./readme-assets/7/137.png)![](./readme-assets/7/147.png)![](./readme-assets/7/157.png)![](./readme-assets/7/167.png)![](./readme-assets/7/177.png)![](./readme-assets/7/187.png)![](./readme-assets/7/197.png)![](./readme-assets/7/207.png)![](./readme-assets/7/217.png)![](./readme-assets/7/227.png)![](./readme-assets/7/237.png)![](./readme-assets/7/247.png)![](./readme-assets/7/257.png)![](./readme-assets/7/267.png)![](./readme-assets/7/277.png)![](./readme-assets/7/287.png)![](./readme-assets/7/297.png)![](./readme-assets/7/307.png)
 
 
##### Samples from Cluster 7
 
 
![](./readme-assets/7/380.png)![](./readme-assets/7/381.png)![](./readme-assets/7/382.png)![](./readme-assets/7/383.png)![](./readme-assets/7/384.png)![](./readme-assets/7/385.png)![](./readme-assets/7/386.png)![](./readme-assets/7/387.png)![](./readme-assets/7/388.png)![](./readme-assets/7/389.png)
 
 
##### Centroids from Cluster 8
 
 
![](./readme-assets/8/008.png)![](./readme-assets/8/018.png)![](./readme-assets/8/028.png)![](./readme-assets/8/038.png)![](./readme-assets/8/048.png)![](./readme-assets/8/058.png)![](./readme-assets/8/068.png)![](./readme-assets/8/078.png)![](./readme-assets/8/088.png)![](./readme-assets/8/098.png)![](./readme-assets/8/108.png)![](./readme-assets/8/118.png)![](./readme-assets/8/128.png)![](./readme-assets/8/138.png)![](./readme-assets/8/148.png)![](./readme-assets/8/158.png)![](./readme-assets/8/168.png)![](./readme-assets/8/178.png)![](./readme-assets/8/188.png)![](./readme-assets/8/198.png)![](./readme-assets/8/208.png)![](./readme-assets/8/218.png)![](./readme-assets/8/228.png)![](./readme-assets/8/238.png)![](./readme-assets/8/248.png)![](./readme-assets/8/258.png)![](./readme-assets/8/268.png)![](./readme-assets/8/278.png)![](./readme-assets/8/288.png)![](./readme-assets/8/298.png)![](./readme-assets/8/308.png)
 
 
##### Samples from Cluster 8
 
 
![](./readme-assets/8/390.png)![](./readme-assets/8/391.png)![](./readme-assets/8/392.png)![](./readme-assets/8/393.png)![](./readme-assets/8/394.png)![](./readme-assets/8/395.png)![](./readme-assets/8/396.png)![](./readme-assets/8/397.png)![](./readme-assets/8/398.png)![](./readme-assets/8/399.png)
 
 
##### Centroids from Cluster 9
 
 
![](./readme-assets/9/009.png)![](./readme-assets/9/019.png)![](./readme-assets/9/029.png)![](./readme-assets/9/039.png)![](./readme-assets/9/049.png)![](./readme-assets/9/059.png)![](./readme-assets/9/069.png)![](./readme-assets/9/079.png)![](./readme-assets/9/089.png)![](./readme-assets/9/099.png)![](./readme-assets/9/109.png)![](./readme-assets/9/119.png)![](./readme-assets/9/129.png)![](./readme-assets/9/139.png)![](./readme-assets/9/149.png)![](./readme-assets/9/159.png)![](./readme-assets/9/169.png)![](./readme-assets/9/179.png)![](./readme-assets/9/189.png)![](./readme-assets/9/199.png)![](./readme-assets/9/209.png)![](./readme-assets/9/219.png)![](./readme-assets/9/229.png)![](./readme-assets/9/239.png)![](./readme-assets/9/249.png)![](./readme-assets/9/259.png)![](./readme-assets/9/269.png)![](./readme-assets/9/279.png)![](./readme-assets/9/289.png)![](./readme-assets/9/299.png)![](./readme-assets/9/309.png)
 
 
##### Samples from Cluster 9
 
 
![](./readme-assets/9/400.png)![](./readme-assets/9/401.png)![](./readme-assets/9/402.png)![](./readme-assets/9/403.png)![](./readme-assets/9/404.png)![](./readme-assets/9/405.png)![](./readme-assets/9/406.png)![](./readme-assets/9/407.png)![](./readme-assets/9/408.png)![](./readme-assets/9/409.png)

#### Distortion Graph
![](./readme-assets/graph.png)
#### Accuracy measure 
To obtain this accuracy measure results are compared to ground truth
![](./readme-assets/accuracy.png)
 
