---
title: 'The ``SHERLOCK PIPEline``: Searching for Hints of Exoplanets fRom Light curves Of spaCe-based seeKers.'
tags:
  - Python
  - Astronomy
  - Exoplanets
  - Kepler
  - K2
  - TESS
authors:
  - name: Francisco J. Pozuelos(*)
    orcid: 0000-0003-1572-7707
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
  - name: Martín Dévora-Pajares(*)
    affiliation: "3, 4"
  - name: Antoine Thuillier
    affiliation: 1
  - name: Valérie Van Grootel
    affiliation: 1
  - name: Luis Cerdeño Mota
    affiliation: 5
  - name: Michaël Gillon
    affiliation: 1
  - name: Juan C. Suarez
    affiliation: 4
 
    
affiliations:
 - name: Space Sciences, Technologies and Astrophysics Research (STAR) Institute, Universitè de Liège, Allée du 6 Août 19C, B-4000 Liège, Belgium
   index: 1
 - name: Astrobiology Research Unit, Universitè de Liège, Allée du 6 Août 19C, B-4000 Liège, Belgium
   index: 2
 - name: Universidad Internacional de Valencia (VIU), Carrer del Pintor Sorolla 21, 46002, Valencia, Spain
   index: 3
 - name: Dpto. Física Teórica y del Cosmos, Universidad de Granada, 18071, Granada, Spain 
   index: 4
 - name: No affiliation
   index: 5
   

date: 15 March 2021
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
# aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
# aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

Transit detection of exoplanets is one of the most fruitful methods for finding planets beyond the Solar System. 
At the time of writing, more than 4,000 exoplanets have been discovered, most of them by the transit method; that is, when a planet passes in front of the disk of its host star it blocks a fraction of the star light, creating a decrease in the observed flux. After the transit, the total
flux rises again to its nominal value.

The transit method was revolutionised by the *Kepler* (and its extended *K2*) mission, which launched in 2009 and operated until 2018. *Kepler* discovered 
more than 2,600 confirmed planets, and its legacy data keep offering exciting results [@niraula:2020; @socia:2020]. Since 2018, another space-based satellite replaced *Kepler* in the hunt for transiting exoplanets: the *TESS* (Transiting Exoplanets Satellite Survey) mission [@ricker:2015]. Different to *Kepler*, which performed its planet search in a reduced portion of the sky, *TESS* is a nearly all-sky survey that focuses on the nearest and brightest stars, searching for planets well suited for, among other science goals, future atmospheric characterization. After completion of its nominal, two-year mission in July 2020, *TESS* started its extended mission, which will last until 2022. During its first two years of operation, *TESS* has released more than 2,000 TOIs (TESS Objects of Interest) and confirmed more than 50 planets. 

Taken together, *Kepler*, *K2* and *TESS*, yield a huge data base of continuous, high-quality observations with excellent photometric precision. 

Motivated to make the most of this considerable abundance of data, in this work we present an open-source pipeline which aims to aid exploration of the data obtained with the aforementioned missions, in the search for new exoplanets. In particular, we are interested in threshold-crossing events, which due to their shallowness remained unnoticed by the current automatic pipelines. 


# 1. The SHERLOCK PIPEline 

The ``SHERLOCK`` (Searching for Hints of Exoplanets fRom Light curves Of spaCe-based seeKers) ``PIPEline``, in short ``SHERLOCK``, is a Python package ready-to-use and user-friendly, which aims to smooth and improve the transiting exoplanets research process by building a unique software to download, search, vet, fit and validate planetary candidates. ``SHERLOCK`` is partially based on previous well-known and well-tested codes used by the exoplanet community to explore the public data gathered by the *Kepler*, *K2* and *TESS* missions without needing to know the finer minutiae of how these data were obtained and stored. In most cases the user only needs to provide a KIC-ID, EPIC-ID, TIC-ID or coordinates of the host star to search for exoplanets. ``SHERLOCK`` has been successfully tested for first time in @pozuelos:2020, @demory:2020 and @benni:2020. 

## 1.1 Searching for candidates

``SHERLOCK`` makes use of the ``LIGHTKURVE`` [@lightkurve:2018], ``WOTAN`` [@wotan:2019], ``ELEANOR`` [@eleanor:2019] and ``TRANSIT LEAST SQUARES`` [@tls:2019] packages to download, process and search for exoplanets in any of the thousands of public light curves provided by *Kepler* and *TESS* missions. Alternatively, the user may provide the light curves in a csv file with "time", "flux" and "flux_err". As output, ``SHERLOCK`` produces a collection of
plots and log files which allow the user to explore the most promising signals. ``SHERLOCK`` uses a multi-detrend approach; that is, it performs a number of detrends by varying the window or the kernel size, depending if the detrending process is bi-weight or Gaussian. Then, ``SHERLOCK`` performs a transit search over the full set of detrended light curves and the original one. This strategy is motivated by the associate risk of removing transit signals, in particular short and shallow ones, during the detrend phase.

The basic usage of ``SHERLOCK`` consists of completing a [properties.yaml](https://github.com/franpoz/SHERLOCK/blob/master/sherlockpipe/properties.yaml) 
file, where the user needs to specify some basic parameters. We encourage the reader to thoroughly consult this file, as well as the examples provided there, to get a firmly understanding of how to effectively use ``SHERLOCK``.

To run ``SHERLOCK``, one only needs to execute: 

```shell
python3 -m sherlockpipe --properties properties.yaml
```

## 1.2 Vetting promising signals

Once the search is done and the user has found a promising candidate, the next step would be to perform some diagnostic tests to check whether the identified signal has an instrumental 
origin and to rule out alternative astrophysical sources. For *TESS* candidates ``SHERLOCK`` uses ``LATTE`` [@eisner:2020], a user-friendly package which examines different aspects such as momentum dumps, background flux, *X-Y* centroid positions, photometric aperture effect, pixel-level centroid analysis, nearby companion stars, nearest-neighbour light curves, and pixel-level light curves. In addition, via ``tpfplotter`` [@aller:2020], a target pixel file is provided, which contains the aperture used to extract the ``PDCSAP`` fluxes (see Section 3.1) and the *Gaia* DR2 catalogue. This allows the user to identify which stars might be affecting the light curve of a given candidate. Collectively, these analyses help the user estimate the reliability of a given detection. In future releases we will extend our vetting tool to *Kepler* and *K2* data. 

Running this vetting tool for a particular signal is as simple as: 
 
```shell 
python3 -m sherlockpipe.vet --candidate {number_of_the_candidate} 

```

by replacing {number_of_the_candidate} with 1, 2, 3, etc., the tool will print a collection of plots. To fully understand these vetting packages, we refer the reader to @eisner:2020, @aller:2020 and @giacalone:2021 respectively.

## 1.3 Validating promising candidates
After the vetting process, it is useful many times to run a bayesian statistical validation of the candidate. Its
star properties, the light curve data and the closest neighbour star properties are passed to a probabilistic model
that assesses the False Positive Probability and Nearby False Positive Probability. ``SHERLOCK`` does it by reading
the candidate data and injecting it to a script that uses ``TRICERATOPS`` [@giacalone:2021]. It testes the alternative 
astrophysical sources estimating the probabilities for different astrophysical scenarios such as transiting planet, 
eclipsing binary, eclipsing binary with 2$\times$ orbital period, among others. As opposite to our vetting tool, 
*Kepler* and *K2* results can be validated thanks to a contribution we have done into the ``TRICERATOPS`` project.

To run the validation the user would need to execute:
```shell
python3 -m sherlockpipe.validate --candidate {number_of_the_candidate}

```

## 1.4 System stability analysis
There are cases where ``SHERLOCK`` could be finding several signals that could form a compact planetary system.
For those situations, ``SHERLOCK`` incorporates a system stability analysis tool that will use ``Rebound`` [] 
and ``SPOCK`` [@tamayo:2020] to compute the stability probabilities. The former uses N-bodies simulations, which we use
to compute the Mean Exponential Growth for Nearby Objects score [@cincotta:2000], meanwhile the latter creates 
pre-trainig machine learning models to assess the system stability probability. For both algorithms we prepare a grid 
of several possible star masses, planet masses and orbit eccentricities to gather at the end a complete report of the 
most stable configurations.
 
To run the stability tool the user would execute: 

```python3 -m sherlockpipe.stability --bodies 1,2,4```

where the `--bodies` parameter is the set of the SHERLOCK accepted signals as CSV to be used in the scenarios 
simulation. You can also provide a 
[stability properties file](https://github.com/franpoz/SHERLOCK/tree/master/examples/properties/stability.yaml))
to run a custom stability simulation:

```python3 -m sherlockpipe.stability --properties stability.yaml```

and you can even combine SHERLOCK accepted signals with some additional bodies provided by the properties file:

```python3 -m sherlockpipe.stability --bodies 1,2,4 --properties stability.yaml```

The results will be stored into a `stability` directory containing the execution log and a `stability.csv`
containing one line per simulated scenario, sorted by the best results scores.

## 1.5 Fitting promising candidates

After the vetting and/or the validation processes, the next step would be to schedule ground-based observations to firmly confirm the event in the target star or to identify potential false positives due to variable stars,
such as an eclipsing binary (EB). To this aim, it is critical to have the most accurate ephemeris as possible. Unfortunately, the solution currently given by the search via ``TLS`` is not optimal to this end, and it is desirable to perform a proper fitting of the transits. There are a number of available public codes which might be used to this end, where ``Juliet`` [@espinoza:2019], ``Exofast`` [@eastman:2019], and ``allesfitter`` [@gunther:2020] are some examples. 
In ``SHERLOCK``, ``allesfitter`` is used. 

To fit a candidate, the user only needs to execute: 
    
```shell 
python3 -m sherlockpipe.fit --candidate {number_of_the_candidate} 

```

Whereby ``SHERLOCK`` saves, jointly with the PDCSAP fluxes, all the light curves generated during the detrending phase. This allows the user the opportunity to use them to fit any other result. 

## 1.6 Creating an observation plan
Once the fitting is done, the candidate could be probably subject to be followed-up by ground-based observations. For that purpose
``SHERLOCK`` includes a tool for suggesting an observation plan selecting the observable future transits given several constaints such as 
the distance and phase of the moon or the observatories coordinates thanks to the usage of the ``Astroplan`` package [@morris:2018]. 
At the end, a ``csv`` is generated with the transit parameters for each provided observatory, whenever the transit is observable from them.

To run the plan generation the next command needs to be executed:
```shell
python3 -m sherlockpipe.plan --candidate {number_of_the_candidate} 
   --observatories observatories.csv
```

# 2. The ``SHERLOCK PIPEline`` workflow  

## 2.1 Data downloading
The light curve within which the user wants to search for exoplanets is downloaded from the NASA Mikulski Archive for Space Telescope (``MAST``). In the case of *TESS* data, the 
Pre-search Data Conditioning Simple APerture (PDCSAP) fluxes given by the ``SPOC`` (Science Process-ing  Operations  Center) are used. For *Kepler* data, the Pre-search Data
Conditioning (PDC) given by the ``SOC`` (Science Operations Center) are used. In both cases, these light curves are corrected for systematic error sources, such as pointing drift,
focus changes and thermal transients. In the case of exploring the full-frame images (FFIs) from *TESS*, the default PCA (Principal Component Analysis) 
fluxes provided by ``ELEANOR`` can be used, although the user can choose among the different available data products such as the raw, corrected, PCA, and PSF-modelled fluxes [@eleanor:2019]. 


## 2.2 Pre-processing of light curve
In many cases the user may find light curves which contain several systematics like noise, high dispersion
near borders, high-amplitude periodicities caused by pulsators, fast rotators, etc. ``SHERLOCK`` 
provides some methods to reduce the effects of these important systematics.

### 2.2.1 Local noise reduction
For local noise, where very close measurements show high deviation from the local trend, we apply a
Savitzky-Golay filter [@sg:1964]. In all our tests, this filter provided a significant improvement of the signal-to-noise ratio (SNR) of previously identified transits.
This implementation is specially interesting in the search for shallow transits. However, the number of false positives is also incremented, and the user needs to verify that 
the proposed signal is realistic, for example checking the transit shape, duration etc. 
This feature can be enabled/disabled by the "INITIAL SMOOTH ENABLED" flag in the [properties.yaml](https://github.com/franpoz/SHERLOCK/blob/master/sherlockpipe/properties.yaml) file.

### 2.2.2 High RMS self-masking
It happens sometimes that a particular region of a given light curve is very noisy, e.g. due to jitter induced by 
the spacecraft, high-light scattering, momentum dumps, etc., which cannot be corrected with a simple detrending process. 
These noisy regions all have high root-mean-square (RMS) noise in comparison with the running mean, and
might have a strongly negative impact on the performance of any pipeline which aims to search for planets, even resulting in all of the potential planets remaining undetected. 
To overcome this issue ``SHERLOCK`` automatically identifies and masks these noisy regions. To this aim, ``SHERLOCK`` includes a binned RMS computation, where bins whose
RMS values are higher than a configurable factor multiplied by the running mean get automatically masked. 
From our experience, appropriate thresholds range from 1.1 to 2.5 times the running mean (see \autoref{fig:rms}).
This feature can be enabled/disabled by the "INITIAL HIGH RMS MASK: True/False" flag. The threshold can be set in the "INITIAL HIGH RMS THRESHOLD" flag. 
Both of these properties are modified in the [properties.yaml](https://github.com/franpoz/SHERLOCK/blob/master/sherlockpipe/properties.yaml) file.

### 2.2.3 Input time-range masking
The user may identify a region with low-quality data where the automatic self-masking 
function is not acting properly. In this situation, the user can manually give the time which should be masked. 
If enabled, this feature automatically disables the automatic self-masking feature.
Some examples are provided in the [properties.yaml](https://github.com/franpoz/SHERLOCK/blob/master/sherlockpipe/properties.yaml) file, in the 
INITIAL MASK module.

### 2.2.4 Automatic detrending of high-amplitude periodicities
Our most common foe with high periodicities are fast-rotators, which impart a highly sinusoidal-like
trend in the PDCSAP fluxes. This is why ``SHERLOCK`` includes an automatic dominant periodicity
detection and detrending during its preparation stage. This feature is controlled by several flags in the 
[properties.yaml](https://github.com/franpoz/SHERLOCK/blob/master/sherlockpipe/properties.yaml) file:
"AUTO DETREND ENABLED", "AUTO DETREND METHOD", "AUTO DETREND RATIO" and "AUTO DETREND PERIOD". The reader is encouraged to consult the examples given 
in the [properties.yaml](https://github.com/franpoz/SHERLOCK/blob/master/sherlockpipe/properties.yaml) file for further 
details and examples.

### 2.2.5 Input period detrending
If the user already knows, for example, that a given target is a fast rotator, and knows its period, this can be directly provided by the user to ``SHERLOCK``.
This input has to be included in the "INITIAL DETREND PERIOD" module in the [properties.yaml](https://github.com/franpoz/SHERLOCK/blob/master/sherlockpipe/properties.yaml) file.
If enabled, this feature automatically disables the automatic detrend of dominant periodicities function. 

## 2.3 Detrending process

Once the pre-processing is done, ``SHERLOCK`` makes use of the ``WOTAN`` package to remove stellar noise, instrumental drifts or any other unwanted trends that may affect the detectability of transiting planets. Two different detrending methods are implemented: 
bi-weight and Gaussian process with a Mat\'ern-3/2 kernel. To optimize the search for transits, the pipeline is run for a number of trials in which the window and kernel sizes 
are varied for each respective aforementioned method. The method used to detrend and the number of trials are set in the "DETRENDS SETUP" module, under the flags "DETREND_METHOD"
and "DETRENDS_NUMBER", respectively. 
The goal of this multi-detrending approach is avoid the potential risk of removing shallow and short transiting signals. While the minimum and maximum window and kernel sizes might be specified
by the user in the [properties.yaml](https://github.com/franpoz/SHERLOCK/blob/master/sherlockpipe/properties.yaml) file, ``SHERLOCK`` offers the option of computing these values automatically: 
the minimum value is obtained by computing the transit duration ($T_{14}$) of a hypothetical Earth-size planet with a period of 15 days orbiting the target star (i.e., to obtain the minimum period, at least 
two transits in one *TESS* sector or one *Kepler* sub-quarter are required). To protect a transit of at least this duration from being removed, we chose a minimum window size of $3\times T_{14}$. 
After conducting experiments, the optimal maximum value explored has been fixed to $20\times T_{14}$, which seemed sufficient to remove low-frecuency variability of most stars. As mentioned previously, these values may be refined by the users, to optimaze their findings. An example of this proccess is displayed in \autoref{fig:detrends}.

![Detrended models applied to a light curve corresponding to TIC 259377017 (in sector 5) with the bi-weight method for twelve different window-sizes. Each panel indicates the window-size in units of days in the top. The black points show the PDCSAP fluxes, the solid-orange lines are the identified trends.\label{fig:detrends}](detrends.png)


## 2.4 The search

For each light curve, ``SHERLOCK`` searches for planet candidates making use the ``TRANSIT LEAST SQUARES`` package, which uses an analytical transit model based on
stellar parameters, and is optimized for the detection of shallow periodic transits [@tls:2019]. ``SHERLOCK`` iteratively executed what we call `runs`. Hence, in each run
the PDCSAP fluxes and the n-detrended light curves that the user indicated in the [properties.yaml](https://github.com/franpoz/SHERLOCK/blob/master/sherlockpipe/properties.yaml)
file are examined. For each light curve, the best periodic signal found jointly with the corresponding periodogram is plotted. That is, if the user used six detrended models, the results of each run will be printed as seven (six-detrended and the PDCSAP flux light curves) `runs plots`, which are saved in specific folders. Moreover, for each light curve, the main results obtained are printed in a log file containing the `period (days)`, `period_err (days)`, `number of transits detected`, `mean depths (ppt)`, `transit duration (min)`, `Epoch (TBJD)`, `Signal-to-noise ratio (SNR)`, `signal detection efficiency (SDE)`, `false alarm probability (FAP)`, `border score`, `Matchin OI`, `Harmonic`, `planet radius` ($R_{\oplus}$), `Rp/Rs`, `Habitability zone`. This information allows the user to evaluate and understand their results. We encourage the reader to thoroughly consult the [examples](https://github.com/franpoz/SHERLOCK/tree/master/examples) in the ``SHERLOCK``'s GitHub site for a better understanding. 

Data close to borders are usually less accurate, and often they have a larger dispersion than the rest of the data. Hence, if a planetary candidate has many of its transits close to borders, this may indicate a false positive. To visualize this effect we included a `border-score` parameter which ranges from 0 to 1, where 
1 means that none of the transits are near the borders, and 0 indicates the opposite. This parameter allows the user to easily identify false positives
in the generated reports.

This part of the code is parallelized, so, making use of ``SHERLOCK`` in a cluster with several cores will considerable speed-up the time of execution. 


## 2.5 Exploring the by-products and results 

``SHERLOCK PIPEline`` produces several information items under a new directory for every analysed object:

* Object report log file: the entire log of the object run is written here.
* Most promising candidates log file: a summary of the parameters of the best transits found for each
run is written at the end of the object execution. 
* Runs directories: for each run of ``SHERLOCK``, a folder will be generated which contains .png images of the detrended fluxes and their suggested transits (\autoref{fig:run}) 

![Example of one detrended light curve which would be stored in the folder `RUN 1`. The header provides the main parameters for the most promising signal. There are three panels, from top to bottom: (1) relative fluxes with the candidate signal overplotted in red; (2) a phase-folded light curve for the candidate. The binning is authomatically chosen to ensure that there will be about 10 points in-transit region. The model for the candidate is given by the solid-red line; and (3) the periodogram where the main period signal and its harmonics are highlighted.\label{fig:run}](example_run1.png)


* Light curve .csv files: original (before pre-processing, that is the PDCSAP fluxes) and all the detrended light curves are saved individualy in .csv files which contain three columns: `#time`, `flux` and `flux_err`.

* Lomb-Scargle Periodogram: this plot corresponds to the Section "(3.2.4) Automatic detrend of high-amplitude periodicities", which shows the period amplitudes (see \autoref{fig:periodogram}).

![Lomb-Scargle Periodogram showing the highest_amplitude of each period.\label{fig:periodogram}](Periodogram.png)

* Phase-folded period: in the case where auto-detrending or manual period detrending is enabled (Sections 3.2.4 and 3.2.5, respectively), it is plotted the phase-folded light curve over the highest-amplitude period in the Lomb-Scargle Periodogram or the period provided by the user, respectively.

![Phase-folded light curve which provides information about the rotational period of the star.\label{fig:autodetrend}](autodetrend.png){width=80%}


* RMS masking plot: In case where the high RMS masking pre-processing step is enabled (Section 3.2.2 and 3.2.3) (see \autoref{fig:rms}).

![Self-masking function evaluates the RMS of the light curve in blocks of four hours and masks these regions with high RMS.\label{fig:rms}](rms.png)


# 3. Performance

To test the performance of ``SHERLOCK`` in comparison to other methods used to finding threshold-crossing events, we carried out a suite of inject-and-recovery experiments using a test *TESS* light curve, corresponding to a single sector. The light curve was injected with a synthetic sample of planets with radii in the range of 0.7 to 2.5 $R_{\oplus}$ with steps of 0.5 $R_{\oplus}$, and periods in the range 0.5-9.5 days, with steps of 0.1 day. In addition, we evaluated each scenario at five different epochs. Hence, in total we evaluated a total of 1710 scenarios. Then, we ran three different methods to find and recover the signals: (1) a search using a classical box least squares algorithm [@kovacs:2002], with an SNR threshold limit of 7 to claim a planet as recovered; (2) a search using the transit least square algorithim, with an SNR threshold limit of 5 to claim a planet as recovered; and (3) a search using ``SHERLOCK`` with an SNR threshold limit of 7, and a maximum of five runs. We found that ``SHERLOCK`` is the most efficient algorithm, being able to recover sub-Earth planets in short-period orbits and about 2 $R_{\oplus}$ for periods as large as 10 days (see \autoref{fig:performance}).

![Comparison between different strategies to search for planets.\label{fig:performance}](sherlock1.png)

In terms of CPU power usage, ``SHERLOCK`` is very intensive, as it searches for transiting exoplanet signals among
several detrended light curves instead of just using one. As many other pipelines from the communities, ``SHERLOCK``
bases this search in the internal usage of ``transitleastsquares``. Despite the improvements of this method in 
comparison to others like box least squares, it increases the computational power (O(n) where n is the number of periods
within the period grid) as the light curve
grows in length. This is an expected scenario for many cases. However, the TESS mission is providing a great amount
of light curves where there are severe data gaps due to the difference of time the measured sectors were scheduled.
For those cases, ``transitleastsquares`` still generates a period grid only based on the time difference between
the last and first points from the light curve. Therefore, its grid becomes highly dense for cases with little
data points, substantially increasing the CPU power (and time) consumption. To avoid this issue, ``SHERLOCK``
incorporates a modified version of ``transitleastsquares`` where the period grid for the search can be externally
provided. That is, ``SHERLOCK`` builds its own period grid only based on the length of the light curve where data 
exists and passes it to ``transitleastsquares``, avoiding large period grids for simple problems and heavily
reducing the CPU power usage of the tool for such cases.   


# 4. Scientific cases 

The ``SHERLOCK PIPEline`` is specially devoted for: 

1) Easily explore public data obtained with space-based observatories. 
2) Find threshold-crossing events that were not reported by the automatic pipelines of *TESS* and *Kepler*.
3) Recover planets already reported, and search for extra candidates in a given system.
4) Search for planets in light curves processed by the user. 
 
That is, ``SHERLOCK`` might be used for a number of projects which need to explore light curves in the search for exoplanets. For example, it is used 
in the *SPECULOOS-TESS* alliance [@sebastian:2021], and in the hot-subdwarf survey in the search for planetary remnants [@vangrootel:2021]
(see the [Hot-subdwarf catalogues](https://github.com/franpoz/Hot-Subdwarfs-Catalogues)).


# 5. Future implementations  

While the  goal of the ``SHERLOCK PIPEline`` is to search for and find planets, there is still a number of improvements which will make the user's life easier. In particular, we have identified some 
relevant features that we are continuously developing and implementing. Here are the most urgent features at the time of writing: 

## 5.1 Pulsating stars

While the automatic detrend of high-amplitude periodicities module (Section 3.2.4) allows the user to remove single pulsation-like features, it is 
very common that stars pulse in different modes, which is more complex than on-period variability. To handle this issue, we will implement a more robust characterization of stellar pulsations. 
In general, high-frequency pulsators which have relatively high amplitudes and can hinder the detection of shallow transits [@sowicka:2017].

## 5.2 Disintegrating planets

We are including in ``SHERLOCK`` a model for comet-like tails of disintegrating exoplanets, which highly differ from the typical shape of transiting exoplanets; see, e.g. [@rappaport:2012,@sanchis:2015]. 

## 5.3 Systems stability
A common analysis to be done to assess a candidate is the calculation of the Mean Exponential Growth of Nearby Orbits (MEGNO) initially introduced by @cincotta:2003. We will analyze a proper way to include such a stability analysis to SHERLOCK by including the ``rebound`` package [@rein:2012] or using ``SPOCK``,
which uses machine learning techniques to improve the results over the MEGNO value for multiplanetary systems as exposed in @tamayo:2020.


## 6. Summary and conclusions

We presented the ``SHERLOCK PIPEline``, a python package to easily search for exoplanets in light curves obtained by space-based missions such as *Kepler*, *K2* and *TESS*, or light curves directly provided by the user. ``SHERLOCK`` has proved to be robust and enfficient, specially suited for the detection of threshold-crossing events that may remain unnoticed by the automatic official pipelines. 
The user only needs to fill the [properties.yaml](https://github.com/franpoz/SHERLOCK/blob/master/sherlockpipe/properties.yaml) file and use three command lines to search, vet, validate, fit and plan observations for the candidates: 

```shell
python3 -m sherlockpipe --properties properties.yaml

python3 -m sherlockpipe.vet --candidate {number_of_the_candidate} 

python3 -m sherlockpipe.validate --candidate {number_of_the_candidate} 

python3 -m sherlockpipe.fit --candidate {number_of_the_candidate}

python3 -m sherlockpipe.plan --candidate {number_of_the_candidate} 
  --observatories observatories.csv

```

After its execution, ``SHERLOCK`` provides a collection of folders, plots and log files containing all the information needed by the user to search and find new exoplanets. 

# Acknowledgements

We acknowledge balblabla


# References
