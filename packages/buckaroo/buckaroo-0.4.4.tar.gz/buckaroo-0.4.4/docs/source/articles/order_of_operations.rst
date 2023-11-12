.. _using:

===================
Order of operations
===================

There are a series of steps for the data in buckaroo


#. Autoclean suggestion pass

   Look at a very samll subset of data to get an idea of the likely column types.  This produces the base of summary_df including the original_dtypes, and type_heruistic_info

#. Autocleaning execution - optional

   Do the actual cleaning.

#. Full summary stats pass

   Perform the full summary summary stats... This should be able to be fused with the autocleaning execution - both essentially require a full table scan.  Prime candidate for widget caching by key of (column-name, column-dtype).  Also amenable to caching because this is an offbranch, the size of cached value will be comparatively small.

#. Filtering

   If configured, filter the data.

#. Sampling

   If after filtering, still too many rows, randomnly downsample to requested size.

#. Lowcode UI interpreter

   Run any user code on the dataframe

#. Secondary summary stats

   Run summary stats again on sampled section.  Only really necessary when filtering enabled, otherwise the full summary stats will be more accurate.

#. Serialize
