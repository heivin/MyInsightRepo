@extends('layouts.default')

<!-- Heading -->
@section('content')
<div class="headingWrapper">
  <!-- Heading -->
  <div class="container adminHeading">
    <span class="text-center">
      <h2><a href="{{ url('/user') }}">Welcome Dude!!</a></h2>
      <p>This is your portal to view your consumption in realtime</p>
    </span>
  </div>
</div>

<!-- Separation -->
<hr/>



@endsection