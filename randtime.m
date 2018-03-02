
function [waits, tseries, P] = randtime(p, n, m)
% This function is set up to simulate a random counting experiment. p is the
% probability of success, n is the number of tries (or atoms collected) and
% m is the number of bins in the histogram.

tseries=rand(n, 1)<= p;%This line creates a matrix of random numbers between 0
%and 1 (rand(n,1)). rand(n,1)<=p checks if that vector is less than the
%input probability p denoting 1 as yes and 0 as no. This vector of 1's and
%0's is stored in the variable tseries.

tvals = tseries.*([1 : n]');%This line creates a vecor where each success is 
%labled by its location in the series

waits = diff([0; tvals(tvals > 0)]);%The wait time vector is found by taking the
%difference of consecutive locations

[pw,wt] = hist(waits, m);%hist creates a histogram where m is the number of bins
%used. pw is the number of times a wait time of wt happened.
%Plotting wt vs. pw will give you the distribution.

P.pw = pw;
P.wt = wt;
end



